# Question 4 : CBC avec IV prévisible
# C1 = AES_k(IV XOR M1), donc si iv2 XOR m0 = iv1 XOR message1, Enc(m0) = CBC_ciphertext
from padding import pad

iv1 = open("data/CBC_iv1", "rb").read()
iv2 = open("data/CBC_iv2", "rb").read()
message1 = pad(open("data/CBC_message1", "rb").read())

m0 = bytes(m ^ a ^ b for m, a, b in zip(message1, iv1, iv2))
m1 = message1

print("m0 =", m0)
print("m1 =", m1)
print("Si c* == CBC_ciphertext alors b' = 0, sinon b' = 1")
