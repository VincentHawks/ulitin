from src.damage import Damage, Resists
from src.entity import Entity, Player


def maths_behavior(target: Player):
    target.get_attack().set_math(10)


def maths_cancel_behavior(target: Player):
    target.get_attack().set_math(0)


def gift_behavior(target: Entity):
    for ability in target.get_abilities():
        ability.set_cooldown_effect(2)


def headphones_behavior(target: Player):
    target.get_resists().set_phil(0.75)


def headphones_cancel_behavior(target: Player):
    target.get_resists().set_phil(0.1)


def cigarette_behavior(target: Player):
    ability_pool = [a for a in target.get_abilities() if a.get_level() <= 1 and not a.is_avalaible()]
    print("Вы можете восстановить одну из следующих спосбоностей:")
    index = 1
    for ability in ability_pool:
        print(index + '.', ability.get_name())
        index += 1
    while True:
        try:
            decision = int(input('?: '))
            break
        except ValueError:
            print("Попробуйте еще раз.")
    target.get_abilities()[target.get_abilities().index(ability_pool[decision-1])].reset_cooldown()


def adrenaline_behavior(target: Player):
    ability_pool = [a for a in target.get_abilities() if a.get_level() <= 2 and not a.is_avalaible()]
    print("Вы можете восстановить одну из следующих спосбоностей:")
    index = 1
    for ability in ability_pool:
        print(index + '.', ability.get_name())
        index += 1
    while True:
        try:
            decision = int(input('?: '))
            break
        except ValueError:
            print("Попробуйте еще раз.")
    target.get_abilities()[target.get_abilities().index(ability_pool[decision-1])].reset_cooldown()


def drugs_behavior(target: Player):
    ability_pool = [a for a in target.get_abilities() if a.get_level() <= 3 and not a.is_avalaible()]
    print("Вы можете восстановить одну из следующих спосбоностей:")
    index = 1
    for ability in ability_pool:
        print(index + '.', ability.get_name())
        index += 1
    while True:
        try:
            decision = int(input('?: '))
            break
        except ValueError:
            print("Попробуйте еще раз.")
    target.get_abilities()[target.get_abilities().index(ability_pool[decision-1])].reset_cooldown()


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


def phone_behavior(target: Player):
    print('''Вы можете увеличить один тип урона на 8. Выберите вид урона.
1. Физический
2. Математический
3. Философский
4. Программистский''')
    while True:
        decision = input('?: ')
        if decision is '1':
            target.get_attack().set_phys(target.get_attack().get_phys() + 8)
            break
        elif decision is '2':
            target.get_attack().set_math(target.get_attack().get_math() + 8)
            break
        elif decision is '3':
            target.get_attack().set_phil(target.get_attack().get_phil() + 8)
            break
        elif decision is '4':
            target.get_attack().set_prog(target.get_attack().get_prog() + 8)
            break
        else:
            print("Попробуйте еще раз")
    phone_choice = decision


def phone_cancel_behavior(target: Player):
    if phone_choice is '1':
        target.get_attack().set_phys(target.get_attack().get_phys() - 8)
    elif phone_choice is '2':
        target.get_attack().set_math(target.get_attack().get_math() - 8)
    elif phone_choice is '3':
        target.get_attack().set_phil(target.get_attack().get_phil() - 8)
    elif phone_choice is '4':
        target.get_attack().set_prog(target.get_attack().get_prog() - 8)


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
