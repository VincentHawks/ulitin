from src.entity import *
from src.item import shitty_complex, regular_complex, godly_complex
from random import randint


class Location:
    level: int
    name: str

    def __init__(self, name, level, entity: Entity = None, exits=None):
        self.name = name
        self.exits = exits
        self.level = level
        self.entity = entity
        self.exits = exits

    def has_entity(self):
        return self.entity is None

    def tick(self):
        self.entity.tick()


class Cafeteria(Location):

    def __init__(self):
        super().__init__("Столовая", 1)
        self.menu = [shitty_complex, regular_complex, godly_complex]
        self.choice = self.menu[randint(0, 2)]
        self.cooldown_threshold = 20
        self.cooldown = 0
        self.free_complex = True

    def tick(self):
        if self.cooldown > 0:
            self.cooldown -= 1
        else:
            self.choice = self.menu[randint(0, 2)]
            self.cooldown = self.cooldown_threshold

    def shop(self, target: Player):
        print("Добро пожаловать в кафе \"5 минут\"! Что хотели бы приобрести?")
        while True:
            decision = input('1. ' + self.choice.name +
                             ": 100 монет.\n2. Красный компот: 20 монет. \n3. Выход.\n?: ")
            if decision is '1':
                item = self.choice
            elif decision is '2':
                item = red_cumpot
            elif decision is '3':
                return
            try:
                target.deposit(item.price)
                target.give(item)
            except InventoryFull:
                print("Ваш инвентарь полон!")
                target.credit(item.price)
            except InsufficientFunds:
                print("Не хватает денег!")


class Basement(Location):

    def __init__(self):
        super().__init__("Подвал", 1)
        self.shop()

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
basement.exits = [first_floor]
cafeteria.exits = [first_floor]
first_floor.exits = [basement, cafeteria]

