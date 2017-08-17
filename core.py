from random import randint
import random
from random import choice


def new_gladiator(name, health, rage, damage_low, damage_high):
    """ -> (dict)

    Returns dictionary with these values:

    -Health : int between 0 and 100
    -Rage : int between 0 and 100
    -Damage_low : int
    -Damage_high : int
    
    """

    gladiator = {
        'Name': name,
        'Health': health,
        'Rage': rage,
        'Damage_low': damage_low,
        'Damage_high': damage_high
    }

    return gladiator


def new_gladiator2(name, health, rage, damage_low, damage_high):
    """ -> (dict)

    Returns dictionary with these values:

    -Health : int between 0 and 100
    -Rage : int between 0 and 100
    -Damage_low : int
    -Damage_high : int
    
    """

    gladiator = {
        'Name': name,
        'Health': health,
        'Rage': rage,
        'Damage_low': damage_low,
        'Damage_high': damage_high
    }

    return gladiator


def attack(attacker, defender):
    """

    -Each attack can be normal or critical,
    -Crit-chance is the same as attacker's rage(50 rage == 50% crit-chance),
    -Damage is randint() between attacker's damage_low and damage_high,
    -Critting doubles damage dealt,
    -If gladiator crits, rage is reste to 0,
    -If gladiator hits normal, rage is + 15

    """

    attack = randint(attacker['Damage_low'], attacker['Damage_high'])
    rage = attacker['Rage']
    crit = attack * 2

    if randint(1, 100) <= rage:
        defender['Health'] -= crit
        attacker['Rage'] = 0
        message = 'Critical Hit of {}'.format(crit)
    else:
        defender['Health'] -= attack
        attacker['Rage'] += 15
        message = '\nNormal hit of {}'.format(attack)

    return message


def heal(gladiator):
    """

    -Spends 10 rage to heal 5 health,
    -Cannot heal above max health of 100

    """

    if gladiator['Rage'] >= 10:
        gladiator['Rage'] -= 10
        gladiator['Health'] += 5

    return gladiator


def is_dead(gladiator):
    """

    -Returns True iff gladiator has no health.

    """
    if gladiator['Health'] <= 0:
        return True
    return False
