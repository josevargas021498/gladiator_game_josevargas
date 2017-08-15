import core

# def test_new_gladiator():

#     assert new_gladiator(health, rage, damage_low, damage_high) == {
#         'Health': 0,
#         'Damage_high': 30,
#         'Rage': 52,
#         'Damage_low': 20
#     }


def test_is_dead():
    gladiator = 0
    assert core.is_dead(gladiator) == True
