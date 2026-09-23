# Question 4 — Attaque CPA sur le mode CBC à IV prédictible
# Le fichier CBC_ciphertext contient le chiffré du message M1 = « turn to page 01 »
# (CBC_message1), chiffré sous le vecteur CBC_iv1.
# L'émetteur commet l'erreur d'incrémenter son IV de manière prévisible au lieu de
# le tirer aléatoirement ; son prochain IV sera CBC_iv2.
# Quels messages m0 et m1 devez-vous soumettre au challenger lors de l'utilisation
# de CBC_iv2 pour déterminer à coup sûr quel message a été chiffré ?
# Justifiez votre réponse par le calcul du premier bloc de chiffrement CBC.

iv1 = open('data/CBC_iv1', 'rb').read()
iv2 = open('data/CBC_iv2', 'rb').read()
message1 = open('data/CBC_message1', 'rb').read() + b'\0'  # pad a 16 octets

# on veut iv2 xor m0 = iv1 xor message1
m0 = b''
for i in range(16):
    m0 = m0 + bytes([message1[i] ^ iv1[i] ^ iv2[i]])
m1 = message1

print('m0 =', m0)
print('m1 =', m1)
