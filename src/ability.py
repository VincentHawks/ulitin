from src.entity import *
from src.damage import *

class Ability:
    def __init__(self, name: str, description: str, level: int, cooldown: int, damage: Damage, heal: int,
                 resist: Resists, passive=False, duration = 0, special_behavior=None, cancel_behavior=None):
        self.name = name
        self.description = description
        self.level = level
        self.cooldown_threshold = cooldown
        self.cooldown = 0
        self.damage = damage
        self.heal = heal
        self.resist = resist
        self.behavior = special_behavior
        self.cancel_behavior = cancel_behavior
        self.passive = passive
        self.duration_threshold = duration
        self.duration = 0
        self.cooldown_effect = 0
        self.target = None

    
    # TODO consider rewriting completely
    def tick(self):
        if self.cooldown > 0:
            self.cooldown -= 1
        if self.duration > 0:
            self.duration -= 1
        if self.duration == 0 and self.passive:
            self.cooldown = self.cooldown_threshold + 1 + self.cooldown_effect
            self.stop_behavior()

  

    # TODO rewrite completely
    def use(self, target: Entity):
        target.damage(self.damage)
        target.heal(self.heal)
        self.apply_behavior(target)
        if self.passive:
            self.duration = self.duration_threshold
            target.activate_ability(self)
        self.cooldown = self.cooldown_threshold + 1 + self.cooldown_effect


# Define the abilities
whine = Ability("Поныть в беседе",
                "Способность 1 уровня. Поныть о тяжестях жизни, +20% к сопротивляемости математическому, философскому и программистскому урону на 3 хода. Перезарядка - 3 хода",
                1, 3, Damage(0, 0, 0, 0, 0), 0, Resists(0, 0.2, 0.2, 0.2),
                True, 3)
laba = Ability("Сдать лабу",
               "Способность 1 уровня. Вы сдаете лабу по проге, наносит 30 прог урона. Перезарядка - 3 хода", 1, 3,
               Damage(0, 0, 0, 30, 0),
               0, Resists(0, 0, 0, 0), False, 0)
speak_to_elders = Ability("Поговорить со старшими курсами",
                        "Способность 1 уровня. Запрос помощи у старших курсов. Повышает сопротивление к программистскому (15%) и математическому (15%) уронам на 3 хода. Перезарядка - 4 хода",
                        1, 4, Damage(0, 0, 0, 0, 0), 0, Resists(0, 0.15, 0, 0.15), True, 3)
make_meme = Ability("Сделать мем", "Вы делаете мем про вышку. Наносит 15 философского урона. Перезарядка - 2 хода", 1, 2,
                   Damage(0, 0, 15, 0, 0), 0, Resists(0, 0, 0, 0), False, 0)
do_homework = Ability("Сделать домашку",
                     "Способность 1 уровня. Вы делаете домашнее задание по матеше. Наносит 10 математического урона. Перезарядка - 1 ход",
                     1,
                     1,
                     Damage(0, 10, 0, 0, 0), 0, Resists(0, 0, 0, 0), False, 0)
sleep = Ability("Выспаться",
                "Способность 1 уровня. Вы решили классно поспать. Восстанавливает 30 здоровья, повышает сопротивление к философскому урону на 20% на 3 хода. Перезарядка -  4 хода",
                1, 4, Damage(0, 0, 0, 0, 0), 30, Resists(0, 0, 0.20, 0), True, 3)

whine_to_headman = Ability("Настучать старосте",
                         "Способность 1 уровня. Вы жалуетесь старосте на свою сложную жизнь. Наносит 7 философского урона и 5 физического урона. Перезарядка - 2 хода",
                         1, 2, Damage(5, 0, 7, 0), 0, Resists(0, 0, 0, 0), False, 0)
take_photo = Ability("Сделать фото на фоне Вышки",
                    "Способность 1 уровня. Вы фоткаетесь на фоне ВШЭ, чтобы показать какой вы классный. Вы получаете неуязвимость ко всем видам урона (кроме чистого) на 1 ход. Пеоезарядка - 5 ходов",
                    1, 5, Damage(0, 0, 0, 0, 0), 0, Resists(1, 1, 1, 1), True, 1)

complete_coursework_second = Ability(
    "Сдать курсач (2 курс)",
    "Способность 2 уровня. Вы сдаете курсовую работу. Наносит 25 чистого урона. Перезарядка - 4 хода", 2, 4,
    Damage(0, 0, 0, 0, 25),
    0, Resists(0, 0, 0, 0), False, 0)

whine_to_dean = Ability("Настучать в деканат",
                      "Способность 2 уровня. Вы жалуетесь а тяжелую жизнь декану. Наносит 15 философского урона и 5 физического урона. Перезарядка - 3 хода",
                      2, 3, Damage(5, 0, 15, 0, 0), 0, Resists(0, 0, 0, 0), False, 0)
drink_with_groupmates = Ability("Бухнуть с одногоуппниками",
                              "Способность 2 уровня. Восстанавливает 70 здоровья, повышает сопротивление к философскому урону на 25%, уменьшает сопротивление игрока к физическому и математическому урону на 40% на 3 хода. Перезарядка - 5 ходов",
                              2, 5, Damage(0, 0, 0, 0, 0), 70, Resists(-0.4, -0.4, 0.25, 0), True, 3)
check_github = Ability("Пошерстить GitHub",
                      "Способность 2 уровня. Вы пытаетесь найти решение на гитхабе. Наносит 35 программистского урона. Перезарядка - 4 хода",
                      2, 4, Damage(0, 0, 0, 35, 0), 0, Resists(0, 0, 0, 0), False, 0)
survive_resit = Ability("Пережить пересдачу",
                       "Способность 2 уровня. Вы стойко переживаете пересдачу. Наносит 20 математического урона и 20 философского урона. Перезарядка - 4 хода",
                       2, 4, Damage(0, 20, 20, 0, 0), 0, Resists(0, 0, 0, 0), False, 0)
# не ясно как реализовать возвращение нанесенного урона
'''
argue = Ability("Поспорить с преподом",
                   "Способность 2 уровня. Вы пытаетесь поспорить с преподавателем. В следующий ход возвращает противнику 25% нанесенного им урона (кроме чистого). Перезарядка -  4 хода",
                   2, 4, Damage(0, 0, 0, 0, 0), 0, Resists(0, 0, 0, 0), True, 1)
'''

complete_coursework_third = Ability("Сдать курсач (3 курс)",
                                  "Способность 3 уровня. Вы сдаете курсовую работу. Наносит 50 чистого урона. Перезарядка - 7 ходов",
                                  3, 7,
                                  Damage(0, 0, 0, 0, 50), 0, Resists(0, 0, 0, 0), False, 0)

whine_to_rector = Ability("Настучать ректору",
                        "Способность 3 уровня. Вы жалуетесь ректору на все, что можно. Наносит 30 философского урона и 10 физического урона. Перезарядка - 4 хода",
                        3, 4, Damage(10, 0, 30, 0, 0), 0, Resists(0, 0, 0, 0), False, 0)

change_minor = Ability("Сменить майнор",
                      "Способность 3 уровня. Вы меняете майнор. Наносит 20 философского урона, восстанавливает вам 40 здоровья. Перезарядка - 6 ходов.",
                      3, 6,
                      Damage(0, 0, 20, 0, 0), 40, Resists(0, 0, 0, 0), False, 0)

check_stackoverflow = Ability("Пошерстить Stackoverflow",
                             "Способность 3 уровня. Вы пытаетесь найти решение на стековерфлоу. Наносит 60 программистского урона. Перезарядка - 6 ходов",
                             3, 6, Damage(0, 0, 0, 60, 0), 0, Resists(0, 0, 0, 0), False, 0)

complete_diploma = Ability("Сдать диплом",
                          "Способность 4 уровня. Вы сдаете диплом. Убивает вашего противника. Перезарядка - 15 ходов.",
                          4, 15,
                          Damage(0, 0, 0, 0, 1000), 0, Resists(0, 0, 0, 0), False, 0)
# не ясно как реализовывать возврат урона
'''
somebodys_child = Ability("Кое-чей ребенок",
                        "Способность 4 уровня. Вы родились под правилььным знаком. Возвращает противнику 50% наносимого им урона. Длительность - 3 хода. Перезарядка - 7 ходов",
                        4, 7, Damage (0,0,0,0,0), 0, Resists(0,0,0,0), True, 3)
'''
