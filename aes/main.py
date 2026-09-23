# TP 1 — INFO731
# Première partie : Chiffrement par blocs et modes opératoires
#
# Préambule : Prise en main et bourrage (padding)
# Un chiffrement par blocs comme AES traite des blocs de taille fixe (16 octets).
# Pour chiffrer des données de taille arbitraire, le message doit être complété
# par un bourrage avant le chiffrement, puis débarrassé de ce bourrage après le
# déchiffrement.

from Crypto.Cipher import AES
from Crypto import Random


def pad(s):
    """Takes in a string, and returns that string with zeros appended.
    Padding should be performed prior to encryption.
    """
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)


def unpad(s):
    """Removes trailing zeros from a string.
    Unpadding should be performed after decryption.
    """
    return s.rstrip(b"\0")


THIS_MODE = AES.MODE_ECB
KEY_SIZE = AES.key_size[0]
# cle secrete de 16 octets
key = Random.new().read(KEY_SIZE)
# iv de 16 octets (sert pour CBC, pas pour ECB)
iv = Random.new().read(AES.block_size)

X = b"A" * AES.block_size
Y = b"B" * AES.block_size
print(X)
print(Y)
# 1. L'Adversaire prépare m0 et m1 (chacun fait 2 blocs, soit 32 octets)
m0 = X + X  # m0 = X || X (deux blocs identiques)
m1 = X + Y  # m1 = X || Y (deux blocs différents)
cipher = AES.new(key, THIS_MODE)

ciphertext = cipher.encrypt(m1)
print(ciphertext.hex())




# 2. Le challenger chiffre m_b ; l'adversaire compare les deux blocs du chiffre
b = Random.new().read(1)[0] & 1
c = cipher.encrypt([m0, m1][b])
b_guess = 0 if c[:16] == c[16:32] else 1
print("b =", b, "/ b' =", b_guess, "->", "gagne" if b == b_guess else "perdu")
