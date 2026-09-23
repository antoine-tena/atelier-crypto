# Question 7 : attaque par espace de messages réduit sur Textbook RSA
from Crypto.PublicKey import RSA

import tools

public_key = RSA.import_key(open("data/part2_key.pub").read())
ctext = int(open("data/part2_ctext").read().strip("()L,\n "))  # format "(123...L,)"

for m in open("data/part2_messagespace").read().splitlines():
    if pow(tools.text_to_int(m), public_key.e, public_key.n) == ctext:
        print("Message :", m)
