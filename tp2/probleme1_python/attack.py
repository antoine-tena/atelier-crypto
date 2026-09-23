# Lab Isolation - Probleme 1 : Python n'isole rien.
# Chaque attaque exploite une chose differente partagee avec le grader.
import sys
import os
import gc


def attack_one(guess):
    # guess est une fermeture qui capture `secret` ; on lit la cellule capturee.
    return guess.__closure__[0].cell_contents


def attack_two():
    # `secret` est une variable locale de l'appelant (scenario_two) ; on lit sa frame.
    return sys._getframe(1).f_locals["secret"]


def attack_three():
    # On est appele AVANT que secret = os.urandom(256) soit execute.
    # On detourne os.urandom pour qu'il renvoie une valeur connue.
    v = bytes(256)
    os.urandom = lambda n: v
    return v


def attack_four():
    # L'objet SecretStore n'est plus reference que par son cycle self.myself,
    # donc il n'est pas collecte : on le retrouve dans le tas via gc.
    for o in gc.get_objects():
        if type(o).__name__ == "SecretStore":
            return o.secret
