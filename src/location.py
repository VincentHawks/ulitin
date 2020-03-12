from src.entity import *
from src.item import shitty_complex, regular_complex, godly_complex
from random import randint

class Location:
    __level: int
    __name: str

    def __init__(self, name, level, entity: Entity = None, exits=None):
        self.__name = name
        self.__exits = exits
        self.__level = level
        self.__entity = entity
        self.__exits = exits

    def get_level(self):
        return self.__level

    def get_name(self):
        return self.__name

    def get_exits(self):
        return self.__exits

    def get_entity(self):
        return self.__entity

    def populate_exits(self, exits: list):
        self.__exits = exits

    def insert_entity(self, entity: Entity):
        self.__entity = entity

    def kill_entity(self):
        self.__entity = None

    def has_entity(self):
        return self.__entity is None

    def tick(self):
        self.__entity.tick()


class Cafeteria(Location):

    def __init__(self):
        super().__init__("Столовая", 1)
        self.__menu = [shitty_complex, regular_complex, godly_complex]
        self.__choice = self.__menu[randint(0, 2)]
        self.__cooldown_threshold = 20
        self.__cooldown = 0
        self.__free_complex = True

    # Just to be safe
    def insert_entity(self, entity: Entity):
        pass

    def has_entity(self):
        return False

    def kill_entity(self):
        pass

    def tick(self):
        if self.__cooldown > 0:
            self.__cooldown -= 1
        else:
            self.__choice = self.__menu[randint(0, 2)]
            self.__cooldown = self.__cooldown_threshold

    def shop(self, target: Player):
        print("Добро пожаловать в кафе \"5 минут\"! Что хотели бы приобрести?")
        while True:
            decision = input('1. ' + self.__choice.get_name() +
                             ": 100 монет.\n2. Красный компот: 20 монет. \n3. Выход.\n?: ")
            if decision is '1':
                item = self.__choice
            elif decision is '2':
                item = red_cumpot
            elif decision is '3':
                return
            try:
                target.deposit(item.get_price())
                target.give(item)
            except InventoryFull:
                print("Ваш инвентарь полон!")
                target.credit(item.get_price())
            except InsufficientFunds:
                print("Не хватает денег!")


class Basement(Location):

    def __init__(self):
        super().__init__("Подвал", 1)
        self.shop()

    # Just to be safe
    def insert_entity(self, entity: Entity):
        pass

    def has_entity(self):
        return False

    def kill_entity(self):
        pass

    # TODO implement
    def shop(self):
        pass


class Auditory(Location):
    def __init__(self, level, number):
        super().__init__("Аудитория " + number, level)


# Define the locations
basement = Basement()
first_floor = Location("Первый этаж", 1)
cafeteria = Cafeteria()

# Now link all of the locations together
basement.populate_exits([first_floor])
cafeteria.populate_exits([first_floor])
first_floor.populate_exits([basement, cafeteria])

