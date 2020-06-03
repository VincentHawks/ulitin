from src.ability import Ability
from src.item import *
from random import randint
from src.location import Location


class Dead(Exception):
    def __init__(self):
        super().__init__()


class Entity:

    def __init__(self, name, level, attack: Damage, abilities: list, health: int, resists: Resists):
        self.name = name
        self.level = level
        self.attack = attack
        self.abilities = abilities
        self.health_constraint = health
        self.health = health
        self.resists = resists
        self.active_abilities = []

    def add_resists(self, resists: Resists):
        self.resists.set_math(self.resists.get_math() + resists.get_math())
        self.resists.set_phys(self.resists.get_phys() + resists.get_phys())
        self.resists.set_phil(self.resists.get_phil() + resists.get_phil())
        self.resists.set_prog(self.resists.get_prog() + resists.get_prog())

    def subtrat_resists(self, resists: Resists):
        self.resists.set_math(self.resists.get_math() - resists.get_math())
        self.resists.set_phys(self.resists.get_phys() - resists.get_phys())
        self.resists.set_phil(self.resists.get_phil() - resists.get_phil())
        self.resists.set_prog(self.resists.get_prog() - resists.get_prog())

    def attack(self, target):
        return target.damage(self.attack)

    def damage(self, damage: Damage):
        effective_damage = int(damage.get_math() * (1 - self.resists.get_math() if self.resists.get_math() <= 1 else 0) +
                               damage.get_phys() * (1 - self.resists.get_phys() if self.resists.get_phys() <= 1 else 0) +
                               damage.get_phil() * (1 - self.resists.get_phil() if self.resists.get_phil() <= 1 else 0) +
                               damage.get_prog() * (1 - self.resists.get_prog() if self.resists.get_prog() <= 1 else 0) +
                               damage.get_abs())
        self.health -= effective_damage
        if self.health <= 0:
            raise Dead
        return effective_damage

    def heal(self, amount):
        self.health += amount
        if self.health > self.health_constraint:
            self.health = self.health_constraint

    def activate_ability(self, index: int):
        ability = self.abilities[index]
        if ability.is_passive():
            self.active_abilities.append(ability)

    def tick(self):
        for ability in self.abilities:
            ability.tick()
        for ability in self.active_abilities:
            if ability.get_duration() == 0:
                self.active_abilities.remove(ability)
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
        super().__init__(name, 1, Damage(10, 0, 0, 0, 0),
                         [], 120, Resists(0.1, 0.1, 0.1, 0.1))
        self.head = None
        self.hand = None
        self.body = None
        self.items = []
        self.location = None
        self.money = 0

    # Maybe i messed up real bad here, gotta see. This one is hella complicated
    def use_item(self, item):
        # First check whether we have an index or an object copy
        if isinstance(item, int):
            item_object = self.items[item]
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
            if self.head is not None:
                self.head.unuse(self)
                self.items.append(self.head)
            self.head = item_object
            print("Вы надели на голову", item_object.get_name())
        elif slot is 'hand':
            if self.hand is not None:
                self.hand.unuse(self)
                self.items.append(self.hand)
            self.hand = item_object
            print("Вы взяли в руку", item_object.get_name())
        elif slot is 'body':
            if self.body is not None:
                self.body.unuse(self)
                self.items.append(self.body)
            self.body = item_object
            print("Вы надели", item_object.get_name())
        else:
            # If it does not occupy any slots - simply use it
            print("Вы использовали ", item_object.get_name())
        try:
            # Now apply the effects
            item_object.use(self)
        except Consumed:
            # If that is a consumable, it will signal that it has to be destroyed after using
            self.items.remove(item_object)

    def move(self, location: Location):
        self.location = location

    def deposit(self, amount):
        if amount > self.money:
            raise InsufficientFunds
        self.money -= amount

    def credit(self, amount):
        self.money += amount

    def give(self, item: Item):
        if len(self.items) == 10:
            raise InventoryFull
        self.items.append(item)

    def throw(self, item):
        # First check whether we have an index or an object copy
        if isinstance(item, int):
            item_object = self.items[item]
        elif isinstance(item, Item):
            item_object = item
        else:
            # If neither - something went terribly wrong
            raise ValueError
        self.items.remove(item_object)

    def attack(self, target):
        rv = target.damage(self.attack)
        if self.head is glasses:
            self.heal(rv / 2)
        return rv

    def levelup(self):
        self.level += 1
        self.health_constraint += 10
        self.attack().set_phys(self.attack.get_phys() + 15)


# Nobody should mess with the entity pool
# убирать тут черточки или нет хуй проссышь
__entity_pool = [list() for i in range(4)]
# TODO fill up with desired entities manually


def random_entity(level: int) -> Entity:
    constraint = len(__entity_pool[level-1])
    return __entity_pool[level-1][randint(0, constraint-1)]
