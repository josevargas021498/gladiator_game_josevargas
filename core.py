from random import randint
from random import choice


class Gladiator:
    """ Gladiator Character"""

    def __init__(self, name, health, rage, damage_low, damage_high):
        """Creates Gladiator named "name", health(100), rage(25 of 200),
        damage_low(15), damage_high(30), and special_hit().
        """

        self.name = name
        self.health = health
        self.rage = rage
        self.damage_low = damage_low
        self.damage_high = damage_high

    def __str__(self):
        """(Gladiator) -> str

        Returns str representation of Gladiator.
        """

        return 'Name: {} --- Health: {} --- Rage: {} --- DL: {} --- DH: {}'.center(
            130).format(self.name, self.health, self.rage, self.damage_low,
                        self.damage_high)

    def attack(self, other, move):
        """(Move) -> NoneType
        Returns results of the move slap.
        """
        if self.rage >= move.requirement:
            other.health -= move.damage
            self.rage -= move.requirement
            self.rage += move.benefits
            msg = '\nSuccessful Hit Of {} Damage!'.format(move.damage)
            if move.damage <= 5:
                msg = '{} knew how to stop the hit!'.format(other.name)
            elif move.damage == 0:
                msg = '{} has completely dodged your attack!'.format(
                    other.name)

            return msg

    def heal(self, move):
        if self.rage >= move.requirement:
            self.rage -= move.requirement
            self.health += move.benefits
            if self.health >= 200:
                self.health = 200
            msg = '\nSuccessful Gain Of {} Health!'.format(move.benefits)
            return msg

    def conservative(self, move):
        if self.rage >= move.requirement:
            self.rage += move.benefits
            msg = '\nSuccessful Gain of {} Rage!'.format(move.benefits)
            return msg

    def is_dead(self):
        """(Gladiator) -> bool

        Returns True Iff health is <= 0.
        """

        if self.health <= 0:
            return True

    def health_cheat_code(self):
        """(Gladiator) -> result

        Returns c
        """


class Move:
    """Fighting Move."""

    def __init__(self, name, damage, requirement, benefits):
        """Creates Move named "name", damage power "damage",
        and rage requirement "requirement".
        """

        self.name = name
        self.damage = damage
        self.requirement = requirement
        self.benefits = benefits

    def __str__(self):
        """(Move) -> str
        Returns str representation of Move.
        """

        return '{}--DMG*RANDOM*:{}--RQRMT:{}--BNFT:{}'.format(
            self.name, self.damage, self.requirement, self.benefits)


# class LightweightGladiator(Gladiator):
#     def __init__(self, name, health, rage, damage_low, damage_high,
#                  special_hit):
#         """Creates Gladiator_1 named name, with rage rage,
#         damage_low damage_low, and damage_high damage_high,
#         and special_hit special_hit.
#         """

#         super().__init__(name, health, rage, damage_low, damage_high)
#         special_hit = special_hit

# class HeavyweightGladiator(Gladiator):
#     def __init__(self, name, health, rage, damage_low, damage_high,
#                  special_hit):
#         """Creates Gladiator_1 named name, with rage rage,
#         damage_low damage_low, and damage_high damage_high,
#         and special_hit special_hit.
#         """

#         super().__init__(name, health, rage, damage_low, damage_high)
#         special_hit = special_hit
