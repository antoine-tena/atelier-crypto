# Question 7 — Attaque par espace de messages réduit
from Crypto.PublicKey import RSA
import tools

public_key = RSA.import_key(open('part2_key.pub').read())
n, e = public_key.n, public_key.e

# le fichier contient un tuple Python 2 : "(123...L,)"
ctext = int(open('part2_ctext').read().strip("()L,\n "))

messages = open('part2_messagespace').read().splitlines()

for m in messages:
    if pow(tools.text_to_int(m), e, n) == ctext:
        print("Message trouve :", m)
        break
else:
    print("Aucun message ne correspond")
