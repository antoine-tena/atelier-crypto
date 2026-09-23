# Question 6 : prise en main de RSA et vérification manuelle d'une signature
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15

import tools

key = RSA.generate(2048)
public_key = key.publickey()

# Textbook RSA
message = "I ATE SOME PIE"
m = tools.text_to_int(message)
c = pow(m, public_key.e, public_key.n)
print("Déchiffré :", tools.int_to_text(pow(c, key.d, key.n)))

# Signature PKCS#1 v1.5 puis vérification à la main : s^e mod n
h = SHA256.new(message.encode())
signature = pkcs1_15.new(key).sign(h)
s = int.from_bytes(signature, "big")
print("%0512x" % pow(s, public_key.e, public_key.n))
print("Le suffixe doit être :")
print(h.hexdigest())
