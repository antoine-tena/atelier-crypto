"""Question 7 : attaque par espace de messages réduit sur Textbook RSA."""
from Crypto.PublicKey import RSA
from pathlib import Path

import tools

DATA = Path(__file__).parent / 'data'

public_key = RSA.import_key((DATA / 'part2_key.pub').read_text())
n, e = public_key.n, public_key.e

# le fichier contient un tuple Python 2 : "(123...L,)"
ctext = int((DATA / 'part2_ctext').read_text().strip("()L,\n "))

messages = (DATA / 'part2_messagespace').read_text().splitlines()

for m in messages:
    if pow(tools.text_to_int(m), e, n) == ctext:
        print("Message trouve :", m)
        break
else:
    print("Aucun message ne correspond")
