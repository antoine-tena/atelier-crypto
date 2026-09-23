from Crypto.Cipher import AES
from Crypto import Random


def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)


key = Random.new().read(AES.key_size[0])
iv = Random.new().read(AES.block_size)

f = open('data/tux6.ppm', 'rb')
lignes = f.read().split(b'\n', 3)
f.close()

# les 3 lignes d'en-tete restent en clair
entete = lignes[0] + b'\n' + lignes[1] + b'\n' + lignes[2] + b'\n'
image = lignes[3]

# Question 1 — Chiffrement d'une image en mode ECB
# Le fichier tux6.ppm contient une image au format PPM binaire non compressé.
# - Isolez les trois premières lignes d'en-tête du fichier tux6.ppm.
# - Chiffrez l'ensemble des octets de données de pixels en utilisant AES en mode ECB.
# - Recollez l'en-tête non chiffré au début des données chiffrées et enregistrez le fichier produit.
# - Ouvrez l'image obtenue et décrivez ce que vous observez visuellement.
cipher = AES.new(key, AES.MODE_ECB)
f = open('rendu/tux_ecb.ppm', 'wb')
f.write(entete + cipher.encrypt(pad(image)))
f.close()

# Question 2 — Chiffrement d'une image en mode CBC
# - Répétez l'opération précédente sur tux6.ppm en utilisant cette fois le mode CBC
#   avec un vecteur d'initialisation (IV) aléatoire.
# - Enregistrez le fichier obtenu avec son en-tête d'origine en clair.
# - Comparez le résultat visuel avec l'image issue du chiffrement ECB de la Question 1.
cipher = AES.new(key, AES.MODE_CBC, iv)
f = open('rendu/tux_cbc.ppm', 'wb')
f.write(entete + cipher.encrypt(pad(image)))
f.close()
