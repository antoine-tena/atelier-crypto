"""Question 4 : attaque CPA contre CBC quand l'IV est prévisible.

Premier bloc CBC : C1 = AES_k(IV XOR M1).
On choisit m0 tel que iv2 XOR m0 = iv1 XOR M1, donc Enc(m0) sous iv2 = CBC_ciphertext.
"""
from pathlib import Path

from padding import pad

DATA = Path(__file__).parent / "data"

iv1 = (DATA / "CBC_iv1").read_bytes()
iv2 = (DATA / "CBC_iv2").read_bytes()
message1 = pad((DATA / "CBC_message1").read_bytes())  # 15 octets -> 16

m0 = bytes(m ^ a ^ b for m, a, b in zip(message1, iv1, iv2))
m1 = message1

print("iv1 XOR iv2 =", bytes(a ^ b for a, b in zip(iv1, iv2)).hex())
print("m0 =", m0)
print("m1 =", m1)
print("Si c* == CBC_ciphertext alors b' = 0, sinon b' = 1")
