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

    print('\nLET\'S FIIIIIIGGGHHHTTT!!!\n\n')
    time.sleep(1)

    gladiator_1 = core.new_gladiator('Chicharito', health, rage, damage_low,
                                     damage_high)
    gladiator_2 = core.new_gladiator2('Messy', health, rage, damage_low,
                                      damage_high)
    while True:
        print('----------------------------------------------------------')
        print('|{}: HP {}, Rage {}, || {}: Hp {}, Rage {}| '.format(
            gladiator_1['Name'], gladiator_1['Health'], gladiator_1['Rage'],
            gladiator_2['Name'], gladiator_2['Health'], gladiator_2['Rage']))

        print('----------------------------------------------------------')

        print('\nIt is ' + gladiator_1['Name'] + '\'s turn!')
        time.sleep(1)

        decision_1 = slow_type(
            '\n\nWhat do you want to do? \n\n\n1.Attack\n\n2.Heal\n\n: ')
        if decision_1 == '1':
            core.attack(gladiator_1, gladiator_2)
            # print(status)
            time.sleep(1)
        elif decision_1 == '2':
            core.heal(gladiator_1)
            # print(status)

        print('\n\nIt\'s Messy\'s Turn!\n')
        time.sleep(1)
        decision_2 = slow_type(
            '\n\nWhat do you want to do? \n\n\n1.Attack\n\n2.Heal\n\n: ')

        if decision_2 == '1':
            core.attack(gladiator_2, gladiator_1)
            time.sleep(1)
        elif decision_2 == '2':
            core.heal(gladiator_2)
            # print(status)


if __name__ == '__main__':
    main()