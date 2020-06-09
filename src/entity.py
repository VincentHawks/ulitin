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
        self.damage = attack
        self.abilities = abilities
        self.health_constraint = health
        self.health = health
        self.resists = resists
        self.active_abilities = []  # As in "currently activated"

    def add_resists(self, resists: Resists):
        self.resists.math += resists.math
        self.resists.phys += resists.phys
        self.resists.phil += resists.phil
        self.resists.prog += resists.prog

    def subtract_resists(self, resists: Resists):
        self.resists.math -= resists.math
        self.resists.phys -= resists.phys
        self.resists.phil -= resists.phil
        self.resists.prog -= resists.prog

    def attack(self, target):
        return target.hurt(self.damage)

    def hurt(self, damage: Damage):
        # Negative damage is possible in some cases
        effective_damage = int((damage.math * (1 - self.resists.math if self.resists.math <= 1 else 0) if damage.math > 0 else 0) +
                               (damage.phys * (1 - self.resists.phys if self.resists.phys <= 1 else 0) if damage.phys > 0 else 0) +
                               (damage.phil * (1 - self.resists.phil if self.resists.phil <= 1 else 0) if damage.phil > 0 else 0) +
                               (damage.prog * (1 - self.resists.prog if self.resists.prog <= 1 else 0) if damage.prog > 0 else 0) +
                               damage.abs if damage.abs > 0 else 0)
        self.health -= effective_damage
        if self.health <= 0:
            # Force cancel all active abilities
            for ability in self.active_abilies:
                ability.cancel_behavior(ability.target);
            raise Dead
        return effective_damage

    def heal(self, amount):
        self.health += amount
        # Protection from overhealing
        if self.health > self.health_constraint:
            self.health = self.health_constraint

    # Calling order:
    # Entity.tick() -> Ability.use() -> Entity.activate_ability()

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
                ability.use(self)


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
        slot = item_object.slot

        # Check if wearable (i.e. passive - does not require to be called or updated)
        # If something is in the necessary slot, cancel its behavior first and push it back to the inventory
        # Then place the item in the necessary slot
        if slot is 'head':
            if self.head is not None:
                self.head.unuse(self)
                self.items.append(self.head)
            self.head = item_object
            print("Вы надели на голову", item_object.name)
        elif slot is 'hand':
            if self.hand is not None:
                self.hand.unuse(self)
                self.items.append(self.hand)
            self.hand = item_object
            print("Вы взяли в руку", item_object.name)
        elif slot is 'body':
            if self.body is not None:
                self.body.unuse(self)
                self.items.append(self.body)
            self.body = item_object
            print("Вы надели", item_object.name)
        else:
            # If it does not occupy any slots - simply use it
            print("Вы использовали ", item_object.name)
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
        rv = target.hurt(self.attack)
        if self.head is glasses:
            self.heal(rv / 2)
        return rv

    def levelup(self):
        self.level += 1
        self.health_constraint += 10
        self.attack.phys = self.attack.phys + 15


# Nobody should mess with the entity pool
__entity_pool = [list() for i in range(4)]
# TODO fill up with desired entities manually




def random_entity(level: int) -> Entity:
    constraint = len(__entity_pool[level-1])
    return __entity_pool[level-1][randint(0, constraint-1)]
