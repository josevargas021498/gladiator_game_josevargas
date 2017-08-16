import sys
import time
import core
from random import randint
import random


def main():
    def slow_type(t):
        """
        Returns input() as slowtype,
        typing characters at an
        assigned pace.
        """

        typing_speed = 10

        for l in t:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(typing_speed / 970.0)

        return input()

    health = 100
    rage = 0
    damage_low = 10
    damage_high = 25

    print('\nLETS FIIIIIIGGGHHHTTT!!!\n\n')
    time.sleep(1)

    gladiator_1 = core.new_gladiator(health, rage, damage_low, damage_high)
    gladiator_2 = core.new_gladiator(health, rage, damage_low, damage_high)

    print('Gladiator_1 HP {}, Rage {}, || Gladiator_2 Hp {}, Rage {} '.format(
        gladiator_1['Health'], gladiator_1['Rage'], gladiator_2['Health'],
        gladiator_2['Rage']))

    decision = slow_type('\nWhat do you want to do? \nAttack\nHeal\n: ')


if __name__ == '__main__':
    main()