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
    rage = 100
    damage_low = 10
    damage_high = 25

    print('\nLETS FIIIIIIGGGHHHTTT!!!\n\nHere\'s Your Status: \n')
    time.sleep(1)
    values = core.new_gladiator(health, rage, damage_low, damage_high)
    for key, value in values.items():
        print('- ', key, '---', value)
        time.sleep(.1)
    attacker = values
    defender = values
    x = core.attack(attacker, defender)
    print(x)


if __name__ == '__main__':
    main()