# Question 3 : l'adversaire gagne toujours le jeu CPA contre AES-ECB
import random

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

m0 = b"A" * 16 + b"A" * 16  # deux blocs identiques
m1 = b"A" * 16 + b"B" * 16  # deux blocs différents

victoires = 0
for _ in range(1000):
    # challenger
    key = get_random_bytes(16)
    b = random.randint(0, 1)
    c = AES.new(key, AES.MODE_ECB).encrypt([m0, m1][b])
    # adversaire
    b_devine = 0 if c[:16] == c[16:] else 1
    victoires += b == b_devine

print("Victoires :", victoires, "/ 1000")
