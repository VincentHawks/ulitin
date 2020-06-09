from src.damage import Damage, Resists
from src.entity import Entity, Player


def maths_behavior(target: Player):
    target.attack.math = 10


def maths_cancel_behavior(target: Player):
    target.attack.math = 0


def gift_behavior(target: Entity):
    for ability in target.abilities:
        ability.cooldown_effect = 2


def headphones_behavior(target: Player):
    target.resists.phil = 0.75


def headphones_cancel_behavior(target: Player):
    target.resists.phil = 0.1


def cigarette_behavior(target: Player):
    ability_pool = [a for a in target.abilities if a.level == 1 and not a.is_avalaible()]
    print("Вы можете восстановить одну из следующих спосбоностей:")
    index = 1
    for ability in ability_pool:
        print(index + '.', ability.name)
        index += 1
    while True:
        try:
            decision = int(input('?: '))
            break
        except ValueError:
            print("Попробуйте еще раз.")
    target.abilities[target.abilities.index(ability_pool[decision-1])].cooldown = 0


def adrenaline_behavior(target: Player):
    ability_pool = [a for a in target.abilities if a.level == 2 and not a.is_avalaible()]
    print("Вы можете восстановить одну из следующих спосбоностей:")
    index = 1
    for ability in ability_pool:
        print(index + '.', ability.name)
        index += 1
    while True:
        try:
            decision = int(input('?: '))
            break
        except ValueError:
            print("Попробуйте еще раз.")
    target.abilities[target.abilities.index(ability_pool[decision - 1])].cooldown = 0


def drugs_behavior(target: Player):
    ability_pool = [a for a in target.abilities if a.level == 3 and not a.is_avalaible()]
    print("Вы можете восстановить одну из следующих спосбоностей:")
    index = 1
    for ability in ability_pool:
        print(index + '.', ability.name)
        index += 1
    while True:
        try:
            decision = int(input('?: '))
            break
        except ValueError:
            print("Попробуйте еще раз.")
    target.abilities[target.abilities.index(ability_pool[decision - 1])].cooldown = 0


def tee_behavior(target: Player):
    target.add_resists(Resists(0.15, 0.15, 0.15, 0.15))


def tee_cancel_behavior(target: Player):
    target.subtract_resists(Resists(0.15, 0.15, 0.15, 0.15))


def hoodie_behavior(target: Player):
    target.add_resists(Resists(0.25, 0.25, 0.25, 0.25))


def hoodie_cancel_behavior(target: Player):
    target.subtract_resists(Resists(0.25, 0.25, 0.25, 0.25))


def mantle_behavior(target: Player):
    target.add_resists(Resists(0.5, 0.5, 0.5, 0.5))


def mantle_cancel_behavior(target: Player):
    target.subtract_resists(Resists(0.5, 0.5, 0.5, 0.5))


def crow_behavior(target: Player):
    target.add_resists(Resists(1, 0, 0, 0))


def crow_cancel_behavior(target: Player):
    target.subtract_resists(Resists(1, 0, 0, 0))


phone_choice = ''


# Might not work
def phone_behavior(target: Player):
    print('''Вы можете увеличить один тип урона на 8. Выберите вид урона.
1. Физический
2. Математический
3. Философский
4. Программистский''')
    while True:
        decision = input('?: ')
        if decision is '1':
            target.attack.phys += 8
            phone_choice = decision
            break
        elif decision is '2':
            target.attack.math += 8
            phone_choice = decision
            break
        elif decision is '3':
            target.attack.phil += 8
            phone_choice = decision
            break
        elif decision is '4':
            target.attack.prog += 8
            phone_choice = decision
            break
        else:
            print("Попробуйте еще раз")


def phone_cancel_behavior(target: Player):
    if phone_choice is '1':
        target.attack.phys -= 8
    elif phone_choice is '2':
        target.attack.math -= 8
    elif phone_choice is '3':
        target.attack.phil -= 8
    elif phone_choice is '4':
        target.attack.prog -= 8


def band_behavior(target: Player):
    target.add_resists(Resists(0, 0.2, 0, 0.2))


def band_cancel_behavior(target: Player):
    target.subtract_resists(Resists(0, 0.2, 0, 0.2))


def hat_behavior(target: Player):
    target.add_resists(Resists(0.2, 0, 0.2, 0))


def hat_cancel_behavior(target: Player):
    target.subtract_resists(Resists(0.2, 0, 0.2, 0))


def card_behavior(target: Player):
    for i in range(len(target.get_abilities())):
        target.get_abilities()[i].set_cooldown_effect(1)


def card_cancel_behavior(target: Player):
    for i in range(len(target.get_abilities())):
        target.get_abilities()[i].set_cooldown_effect(0)
