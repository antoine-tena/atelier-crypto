# Questions 1 et 2 : chiffrement de tux6.ppm en ECB puis en CBC
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

from padding import pad

lignes = open("data/tux6.ppm", "rb").read().split(b"\n", 3)
entete = b"\n".join(lignes[:3]) + b"\n"  # les 3 lignes d'en-tête restent en clair
pixels = lignes[3]

key = get_random_bytes(16)

ecb = AES.new(key, AES.MODE_ECB)
open("tux_ecb.ppm", "wb").write(entete + ecb.encrypt(pad(pixels)))

cbc = AES.new(key, AES.MODE_CBC, get_random_bytes(16))
open("tux_cbc.ppm", "wb").write(entete + cbc.encrypt(pad(pixels)))
