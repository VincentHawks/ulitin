from src.entity import *
from src.damage import *

class Ability:
    def __init__(self, name: str, description: str, level: int, cooldown: int, damage: Damage, heal: int,
                 resist: Resists, passive=False, duration = 0, special_behavior=None, cancel_behavior=None):
        self.__name = name
        self.__description = description
        self.__level = level
        self.__cooldown_threshold = cooldown
        self.__cooldown = 0
        self.__damage = damage
        self.__heal = heal
        self.__resist = resist
        self.__behavior = special_behavior
        self.__cancel_behavior = cancel_behavior
        self.__passive = passive
        self.__duration_threshold = duration
        self.__duration = 0
        self.__cooldown_effect = 0
        self.__target = None

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_level(self):
        return self.__level

    def is_avalaible(self):
        return self.__cooldown == 0

    def is_passive(self):
        return self.__passive

    # TODO consider rewriting completely
    def tick(self):
        if self.__cooldown > 0:
            self.__cooldown -= 1
        if self.__duration > 0:
            self.__duration -= 1
        if self.__duration == 0 and self.__passive:
            self.__cooldown = self.__cooldown_threshold + 1 + self.__cooldown_effect
            self.stop_behavior()

    def get_damage(self):
        return self.__damage

    def get_heal(self):
        return self.__heal

    def get_resist(self):
        return self.__resist

    def apply_behavior(self, target):
        self.__behavior(target)

    def stop_behavior(self, target):

    def reset_cooldown(self):
        self.__cooldown = 0

    def set_cooldown_effect(self, value: int):
        self.__cooldown_effect = value


    # TODO rewrite completely
    def use(self, target: Entity):
        target.damage(self.__damage)
        target.heal(self.__heal)
        self.apply_behavior(target)
        if self.__passive:
            self.__duration = self.__duration_threshold
            target.activate_ability(self)
        self.__cooldown = self.__cooldown_threshold + 1 + self.__cooldown_effect



# Define the abilities
whine = Ability("Поныть в беседе", "Поныть о тяжестях жизни, +20% к сопротивляемости математическому, философскому и программистскому урону на 3 хода",
                1, 3, Damage(0, 0, 0, 0, 0), 0, Resists(0, 0.2, 0.2, 0.2),
                True, 3)