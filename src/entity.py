from src.ability import Ability
from src.item import *
from random import randint
from src.location import Location


class Dead(Exception):
    def __init__(self):
        super().__init__()


class Entity:

    def __init__(self, name, level, attack: Damage, abilities: list, health: int, resists: Resists):
        self.__name = name
        self.__level = level
        self.__attack = attack
        self.__abilities = abilities
        self.__health_constraint = health
        self.__health = health
        self.__resists = resists
        self.__active_abilities = []

    def get_name(self):
        return self.__name

    def get_level(self):
        return self.__level

    def get_abilities(self):
        return self.__abilities

    def get_attack(self):
        return self.__attack

    def get_resists(self):
        return self.__resists

    def add_resists(self, resists: Resists):
        self.__resists.set_math(self.__resists.get_math() + resists.get_math())
        self.__resists.set_phys(self.__resists.get_phys() + resists.get_phys())
        self.__resists.set_phil(self.__resists.get_phil() + resists.get_phil())
        self.__resists.set_prog(self.__resists.get_prog() + resists.get_prog())

    def subtract_resists(self, resists: Resists):
        self.__resists.set_math(self.__resists.get_math() - resists.get_math())
        self.__resists.set_phys(self.__resists.get_phys() - resists.get_phys())
        self.__resists.set_phil(self.__resists.get_phil() - resists.get_phil())
        self.__resists.set_prog(self.__resists.get_prog() - resists.get_prog())

    def attack(self, target):
        return target.damage(self.__attack)

    def damage(self, damage: Damage):
        effective_damage = int(damage.get_math() * (1 - self.__resists.get_math() if self.__resists.get_math() <= 1 else 0) +
                             damage.get_phil() * (1 - self.__resists.get_phil() if self.__resists.get_phil() <= 1 else 0) +
                             damage.get_phys() * (1 - self.__resists.get_phys() if self.__resists.get_phys() <= 1 else 0) +
                             damage.get_prog() * (1 - self.__resists.get_prog() if self.__resists.get_prog() <= 1 else 0) +
                             damage.get_abs())
        self.__health -= effective_damage
        if self.__health <= 0:
            raise Dead
        return effective_damage

    def heal(self, amount):
        self.__health += amount
        if self.__health > self.__health_constraint:
            self.__health = self.__health_constraint

    def activate_ability(self, index: int):
        ability = self.__abilities[index]
        if ability.is_passive():
            self.__active_abilities.append(ability)

    def tick(self):
        for ability in self.__abilities:
            ability.tick()
        for ability in self.__active_abilities:
            if ability.get_duration() == 0:
                self.__active_abilities.remove(ability)
            else:
                ability.use()


class InventoryFull(Exception):
    def __init__(self):
        super().__init__()


class InsufficientFunds(Exception):
    def __init__(self):
        super().__init__()


class Player(Entity):

    def __init__(self, name):
        super().__init__(name, 1, Damage(10, 0, 0, 0, 0), [], 120, Resists(0.1, 0.1, 0.1, 0.1))
        self.__head = None
        self.__hand = None
        self.__body = None
        self.__items = []
        self.__location = None
        self.__money = 0

    # Maybe i messed up real bad here, gotta see. This one is hella complicated
    def use_item(self, item):
        # First check whether we have an index or an object copy
        if isinstance(item, int):
            item_object = self.__items[item]
        elif isinstance(item, Item):
            item_object = item
        else:
            # If neither - something went terribly wrong
            raise ValueError
        slot = item_object.get_slot()

        # Check if wearable (i.e. passive - does not require to be called or updated)
        # If something is in the necessary slot, cancel its behavior first and push it back to the inventory
        # Then place the item in the necessary slot
        if slot is 'head':
            if self.__head is not None:
                self.__head.unuse(self)
                self.__items.append(self.__head)
            self.__head = item_object
            print("Вы надели на голову", item_object.get_name())
        elif slot is 'hand':
            if self.__hand is not None:
                self.__hand.unuse(self)
                self.__items.append(self.__hand)
            self.__hand = item_object
            print("Вы взяли в руку", item_object.get_name())
        elif slot is 'body':
            if self.__body is not None:
                self.__body.unuse(self)
                self.__items.append(self.__body)
            self.__body = item_object
            print("Вы надели", item_object.get_name())
        else:
            # If it does not occupy any slots - simply use it
            print("Вы использовали ", item_object.get_name())
        try:
            # Now apply the effects
            item_object.use(self)
        except Consumed:
            # If that is a consumable, it will signal that it has to be destroyed after using
            self.__items.remove(item_object)

    def move(self, location: Location):
        self.__location = location

    def deposit(self, amount):
        if amount > self.__money:
            raise InsufficientFunds
        self.__money -= amount

    def credit(self, amount):
        self.__money += amount

    def give(self, item: Item):
        if len(self.__items) == 10:
            raise InventoryFull
        self.__items.append(item)

    def throw(self, item):
        # First check whether we have an index or an object copy
        if isinstance(item, int):
            item_object = self.__items[item]
        elif isinstance(item, Item):
            item_object = item
        else:
            # If neither - something went terribly wrong
            raise ValueError
        self.__items.remove(item_object)

    def attack(self, target):
        rv = target.damage(self.__attack)
        if self.__head is glasses:
            self.heal(rv / 2)
        return rv

    def levelup(self):
        self.__level += 1
        self.__health_constraint += 10
        self.__attack().set_phys(self.__attack.get_phys() + 15)


# Nobody should mess with the entity pool
__entity_pool = [list() for i in range(4)]
# TODO fill up with desired entities manually


def random_entity(level: int) -> Entity:
    constraint = len(__entity_pool[level-1])
    return __entity_pool[level-1][randint(0, constraint-1)]

