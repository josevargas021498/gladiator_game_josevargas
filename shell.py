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

    print('Get..Ready...To...Fight...'.center(135))
    time.sleep(1)
    slow_type('\nPress "ENTER" To Begin!\n')

    jose = core.Gladiator('JoVarg', 200, 30, 15, 30)
    liza = core.Gladiator('LizOstro', 200, 30, 15, 30)

    print('☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠'.center(135))
    print(jose)
    time.sleep(.5)
    print('☠☠☠☠☠☠☠VS☠☠☠☠☠☠☠'.center(135))
    time.sleep(1)
    print(liza)
    print('☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠☠'.center(135))
    time.sleep(1)

    while True:
        print('\n\n\n\n')
        print(jose)
        print('--------------------------------------------------------------'.
              center(135))
        print(liza)

        slap = core.Move('SLAP', randint(0, 25), 15, 20)
        kick = core.Move('KICK', randint(10, 30), 36, 23)
        bite = core.Move('BITE', randint(15, 40), 27, 16)
        slam = core.Move('SLAM', randint(30, 60), 43, 24)
        shoot = core.Move('SHOOT', randint(70, 90), 43, 29)
        conserve = core.Move('CONSERVE', 0, 0, 25)
        heal = core.Move('HEAL', 0, 5, 30)
        liza_sound = core.Move('1.LIZA "AAHHHHH??" SOUND', 100, 60, 45)
        jose_scream = core.Move('2.JOSE "AAEEEEE!!!" SCREAM', 80, 60, 45)

        if jose.is_dead():
            print('⚰⚰⚰⚰⚰⚰⚰⚰⚰⚰⚰⚰⚰⚰⚰⚰⚰'.center(135))
            print('JoVarg! You Are Dead!'.center(135))
            print('⚰⚰⚰⚰⚰⚰⚰⚰⚰⚰⚰⚰⚰⚰⚰'.center(135))
            exit()

        print('\n\n')
        print('-> JoVarg! <- -Make Your Move!-'.center(135))
        print(
            '->👋 {}\n\n->☯ {}\n\n->😁 {}\n\n->💥 {}\n\n->🔫 {}\n\n->♻ {}\n\n->♥ {}\n\n->☢☣💀 {} 💀💀\n\n->♬♬ {}\n\n'.
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
            print('Invalid Choice'.center(135))

        print(message)
        time.sleep(1)

        if liza.is_dead():
            print('⚰⚰⚰⚰⚰⚰⚰⚰⚰⚰⚰⚰⚰⚰⚰⚰⚰'.center(135))
            print('LizOstro! You Are Dead!'.center(135))
            print('⚰⚰⚰⚰⚰⚰⚰⚰⚰⚰⚰⚰⚰⚰⚰⚰⚰'.center(135))
            exit()

        slap = core.Move('SLAP->->', randint(5, 25), 15, 20)
        kick = core.Move('KICK->->', randint(18, 39), 36, 23)
        bite = core.Move('BITE->->', randint(27, 51), 27, 16)
        slam = core.Move('SLAM->->', randint(45, 70), 43, 34)
        shoot = core.Move('SHOOT->->', randint(70, 90), 43, 40)
        conserve = core.Move('CONSERVE->->', 0, 0, 25)
        heal = core.Move('HEAL->->', 0, 5, 30)
        liza_sound = core.Move('\n1.LIZA "AAHHHHH??" SOUND', 100, 60, 45)
        jose_scream = core.Move('\n2.JOSE "AAEEEE!!!" SCREAM', 90, 60, 45)

        print('\n\n')
        print('-> LizOstro! <- -Make Your Move!-'.center(135))
        print(
            '->👋 {}\n\n->☯ {}\n\n->😁 {}\n\n->💥 {}\n\n->🔫 {}\n\n->♻ {}\n\n->♥ {}\n\n->☢☣💀 {} 💀💀\n\n->♬♬ {}\n\n'.
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
            print('Invalid Choice!'.center(135))

        print(message)
        time.sleep(1)


if __name__ == '__main__':
    main()