from src.ability import Ability
from src.entity import Player
from src.damage import *


# Level 1
def kuranova1_behavior(target: Player):
    # Robust and straightforward
    target.damage.math -= 2
    target.damage.phys -= 2
    target.damage.phil -= 2
    target.damage.prog -= 2


def kuranova1_cancel_behavior(target: Player):
    target.damage.math += 2
    target.damage.phys += 2
    target.damage.phil += 2
    target.damage.prog += 2


no_resists = Resists(0, 0, 0, 0)
no_damage = Damage(0, 0, 0, 0, 0)


# Pretty much all of the enemy abilities' descriptions will be empty
kuranova1 = Ability(
    "Менеджер программы", "", 1, 0,
    no_damage, 0, no_resists,
    True, -1, kuranova1_behavior, kuranova1_cancel_behavior
)

kuranova2 = Ability(
    "Не прислать расписание", "", 1, 2,
    Damage(0, 0, 25, 0, 0), 0, no_resists
)

# Basement mob will not be implemented

dima1 = Ability(
    "Устроить самостоятельную", "", 1, 4,
    Damage(0, 30, 0, 0, 0), 0, no_resists
)

tarunina1 = Ability(
    "Коллоквиум", "", 1, 3,
    Damage(0, 0, 30, 0, 0), 0, no_resists
)

linal1 = Ability(
    "Забыть лекции", "", 1, 3,
    Damage(0, 15, 0, 0, 0), 0, no_resists
)

boss111 = Ability(
    "Отправить на пересдачу", "", 1, 4,
    Damage(0, 0, 0, 0, 20), 0, no_resists
)

boss121 = Ability(
    "Менять метод оценивания", "", 1
)

'''
name, description, level, cooldown,
damage: Damage(phys, math, phil, prog, abs), heal: int, resists: Resists,
passive=False, duration=0, special_behavior, cancel_behavior: 
'''