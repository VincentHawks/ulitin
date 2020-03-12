from src.damage import Damage
from src.item_behavior import *


class Consumed(Exception):
    def __init__(self):
        super().__init__()


class Item:
    def __init__(self, name, description, damage: Damage, heal: int, slot: str, rarity: str, price: int,
                 consumable: bool, after_death=False, special_behavior=None, cancel_behavior=None):
        self.__name = name
        self.__description = description
        self.__damage = damage
        self.__heal = heal
        self.__slot = slot
        self.__rarity = rarity
        self.__price = price
        self.__consumable = consumable
        self.__after_death = after_death
        self.__behavior = special_behavior
        self.__cancel_behavior = cancel_behavior

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_damage(self):
        return self.__damage

    def get_heal(self):
        return self.__heal

    def get_slot(self):
        return self.__slot

    def get_rarity(self):
        return self.__rarity

    def get_price(self):
        return self.__price

    def is_used_after_death(self):
        return self.__after_death

    def is_consumable(self):
        return self.__consumable

    def apply_behavior(self, target=None):
        self.__behavior(target)

    # Destruction of consumables is handled by user
    def use(self, target):
        target.damage(self.__damage)
        target.heal(self.__heal)
        self.apply_behavior(target)
        if self.__consumable:
            raise Consumed

    def unuse(self, target):
        self.__cancel_behavior(target)


# Declare the items
maths_records = Item("Конспекты по математическому анализу", "Добавляют 10 математического урона с руки",
                     Damage(0, 0, 0, 0, 0), 0, 'hand', 'common', 0, False, False,
                     maths_behavior, maths_cancel_behavior)
shitty_complex = Item("Невкусный комплекс (перловка с рыбой)", "Восстанавливает 50 здоровья",
                      Damage(0, 0, 0, 0, 0), 50, '', "", 100, True)
regular_complex = Item("Очередной комплекс (гречка с гуляшом)", "Восстанавливает 75 здоровья",
                       Damage(0, 0, 0, 0, 0), 75, '', '', 100, True)
godly_complex = Item("Божественный комплекс (котлетка с пюрешкой)", "Восстанавливает 100 здоровья",
                     Damage(0, 0, 0, 0, 0), 100, '', '', 100, True)
red_cumpot = Item("Красный компот", "Восстанавливает 20 здоровья",
                  Damage(0, 0, 0, 0, 0), 20, '', '', 20, True)
medical_document = Item("Справка от врача", "Спасает от смерти и восстанавливает 50 здоровья",
                        Damage(0, 0, 0, 0, 0), 50, '', 'rare', 0, True)
gift = Item("Подарок", "КД противника увеличивается на 2 хода",
            Damage(0, 0, 0, 0, 0), 0, '', 'epic', 200, True, False,
            gift_behavior)
headphones = Item("Наушники", "Сопротивление философскому урону 75%",
                  Damage(0, 0, 0, 0, 0), 0, 'head', 'epic', 250, False, False,
                  headphones_behavior, headphones_cancel_behavior)
cigarette = Item("Сигарета", "Наносит вам урон, но может полностью восстановить способность 1 уровня на выбор",
                 Damage(0, 0, 0, 0, 7), 0, '', 'common', 10, True, False,
                 cigarette_behavior)
adrenaline = Item("Энергетик", "Наносит вам урон, но может полностью восстановить способность 1 или 2 уровня на выбор",
                  Damage(0, 0, 0, 0, 4), 0, '', 'common', 25, True, False,
                  adrenaline_behavior)
drugs = Item("Запрещенные вещества", "Наносят вам урон, но могут полностью восстановить способность 1, 2 или 3 уровня на выбор",
             Damage(0, 0, 0, 0, 15), 0, '', 'common', 150, True, False,
             drugs_behavior)
hse_tee = Item("Футболка ВШЭ", "Сопротивление всем видам урона +15%",
               Damage(0, 0, 0, 0, 0), 0, 'body', 'rare', 150, False, False,
               tee_behavior, tee_cancel_behavior)
hse_hoodie = Item("Свитшот ВШЭ", "Сопротивление всем видам урона +25%",
                  Damage(0, 0, 0, 0, 0), 0, 'body', 'epic', 250, False, False,
                  hoodie_behavior, hoodie_cancel_behavior)
graduate_mantle = Item("Мантия выпускника", "Сопротивление всем видам урона +50%",
                       Damage(0, 0, 0, 0, 0), 0, 'body', 'legendary', 700, False, False,
                       mantle_behavior, mantle_cancel_behavior)
crow_costume = Item("Костюм вороны", "Сопротивление физическому урону 100%",
                    Damage(0, 0, 0, 0, 0), 0, 'body', 'legendary', 650, False, False,
                    crow_behavior, crow_cancel_behavior)
phone = Item("Телефон", "Добавляет 8 урона выбранного вида",
             Damage(0, 0, 0, 0, 0), 0, 'hand', 'rare', 200, False, False,
             phone_behavior, phone_cancel_behavior)
glasses = Item("Очки зубрилы", "Половина нанесенного противнику урона вернется в виде очков здоровья",
               Damage(0, 0, 0, 0, 0), 0, 'head', 'epic', 300, False)
band = Item("Ободок знаний", "Устойчивость к математическому и программистскому урону +20%",
            Damage(0, 0, 0, 0, 0), 0, 'head', 'rare', 160, False, False,
            band_behavior, band_cancel_behavior)
hat = Item("Шапочка из фольги", "",
           Damage(0, 0, 0, 0, 0), 0, 'head', 'rare', 190, False, False,
           hat_behavior, hat_cancel_behavior)
card = Item("", "",
            Damage(0, 0, 0, 0, 0), 0, 'head', 'epic', 270, False, False,
            card_behavior, card_cancel_behavior)
