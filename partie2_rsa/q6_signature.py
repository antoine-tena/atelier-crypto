"""Question 6 : prise en main de RSA et vérification manuelle d'une signature."""
# (version Python 3 / pycryptodome du script d'exemple)
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15
from pathlib import Path

import tools

ICI = Path(__file__).parent

secparam = 2048

# generation d'une cle RSA
key = RSA.generate(secparam)
public_key = key.publickey()

# sauvegarde puis relecture des cles
open(ICI / 'key.pub', 'wb').write(public_key.export_key())
open(ICI / 'key.priv', 'wb').write(key.export_key())
recovered_public_key = RSA.import_key(open(ICI / 'key.pub', 'rb').read())
assert recovered_public_key == public_key
recovered_key = RSA.import_key(open(ICI / 'key.priv', 'rb').read())
assert recovered_key == key

# chiffrement / dechiffrement Textbook RSA a la main
message = "I ATE SOME PIE"
message_int = tools.text_to_int(message)
n, e, d = public_key.n, public_key.e, key.d
ciphertext = pow(message_int, e, n)
assert pow(ciphertext, d, n) == message_int
assert tools.int_to_text(pow(ciphertext, d, n)) == message

# signature du hash du message avec la cle PRIVEE (PKCS#1 v1.5)
h = SHA256.new(message.encode())
signature = pkcs1_15.new(key).sign(h)
s = int.from_bytes(signature, 'big')

# verification manuelle avec la cle PUBLIQUE : s^e mod n
print("n =", public_key.n)
print("e =", public_key.e)
verif = "%0512x" % pow(s, public_key.e, public_key.n)
print("s^e mod n       :", verif)

# le suffixe de s^e mod n doit etre l'empreinte SHA256 du message
empreinte = SHA256.new(message.encode()).hexdigest()
print("SHA256(message) :", empreinte)
assert verif.endswith(empreinte)
print("Signature valide")

# verification avec la bibliotheque (leve une exception si invalide)
pkcs1_15.new(public_key).verify(h, signature)
