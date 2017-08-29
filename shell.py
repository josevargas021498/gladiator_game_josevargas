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

        typing_speed = 22

        for l in t:
            sys.stdout.write(l)
            sys.stdout.flush()
            time.sleep(typing_speed / 970.0)

        return input()

    print('Get..Ready...To...Fight...'.center(130))
    time.sleep(1)
    slow_type('\nPress "ENTER" To Begin!\n')

    jose = core.Gladiator('JoVarg', 100, 25, 15, 30)
    liza = core.Gladiator('LizOstro', 100, 25, 15, 30)

    print('☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠'.center(130))
    print(jose)
    time.sleep(.5)
    print('☠☠☠☠☠☠☠VS☠☠☠☠☠☠☠'.center(130))
    time.sleep(1)
    print(liza)
    print('☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠'.center(130))
    time.sleep(1)

    while True:
        print('\n\n\n\n')
        print(jose)
        print('--------------------------------------------------------------'.
              center(135))
        print(liza)

        slap = core.Move('Slap', randint(0, 25), 15, 20)
        kick = core.Move('Kick', randint(10, 30), 36, 23)
        bite = core.Move('Bite', randint(15, 40), 27, 16)
        slam = core.Move('Slam', randint(30, 60), 43, 34)
        shoot = core.Move('Shoot', randint(70, 90), 43, 40)
        conserve = core.Move('Conserve', 0, 0, 25)
        heal = core.Move('Heal', 0, 5, 30)
        liza_sound = core.Move('1.Liza AHH? Sound', 100, 60, 45)
        jose_scream = core.Move('2.Jose AEHH! Scream', 80, 60, 45)

        if jose.is_dead():
            print('JoVarg! You Are Dead!'.center(130))
            exit()

        print('\n\n')
        print('-> JoVarg <- -Make Your Move!-'.center(130))
        print(
            '-> {}\n\n-> {}\n\n-> {}\n\n-> {}\n\n-> {}\n\n-> {}\n\n-> {}\n\n-> {}\n\n-> {}\n\n'.
            format(slap, kick, bite, slam, shoot, conserve, heal, liza_sound,
                   jose_scream))
        time.sleep(1)

        choice = slow_type('------->>>>> '.lower())

        if choice == 'slap':
            message = jose.attack(liza, slap)

        elif choice == 'kick':
            message = jose.attack(liza, kick)

        elif choice == 'bite':
            message = jose.attack(liza, bite)

        elif choice == 'slam':
            message == jose.attack(liza, slam)

        elif choice == 'shoot':
            message = jose.attack(liza, shoot)

        elif choice == 'heal':
            message = jose.heal(heal)

        elif choice == 'conserve':
            message = jose.conservative(conserve)

        else:
            print('Invalid Choice'.center(130))

        print(message)
        time.sleep(1)

        if liza.is_dead():
            print('LizOstro! You Are Dead!'.center(130))
            exit()
        print('\n\n')
        print('-> LizOstro <- -Make Your Move!-'.center(130))
        print(
            '-> {}\n\n-> {}\n\n-> {}\n\n-> {}\n\n-> {}\n\n-> {}\n\n-> {}\n\n-> {}\n\n-> {}\n\n'.
            format(slap, kick, bite, slam, shoot, conserve, heal, liza_sound,
                   jose_scream))
        time.sleep(1)

        choice = slow_type('------->>>>> '.lower())

        if choice == 'slap':
            message = liza.attack(jose, slap)

        elif choice == 'kick':
            message = liza.attack(jose, kick)

        elif choice == 'bite':
            message = liza.attack(jose, bite)

        elif choice == 'slam':
            message == liza.attack(jose, slam)

        elif choice == 'shoot':
            message = liza.attack(jose, shoot)

        elif choice == 'heal':
            message = liza.heal(heal)

        elif choice == 'conserve':
            message = liza.conservative(conserve)

            time.sleep(1)
        else:
            print('Invalid Choice!'.center(130))

        print(message)
        time.sleep(1)


if __name__ == '__main__':
    main()