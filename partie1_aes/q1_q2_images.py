"""Questions 1 et 2 : chiffrement de tux6.ppm en AES-ECB puis en AES-CBC.

Les 3 lignes d'en-tête PPM restent en clair pour que l'image reste lisible.
Les images produites sont écrites dans resultats/.
"""
from pathlib import Path

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

from padding import pad

ICI = Path(__file__).parent
SORTIE = ICI / "resultats"


def lire_ppm(chemin: Path) -> tuple[bytes, bytes]:
    """Sépare l'en-tête (3 premières lignes) des données de pixels."""
    lignes = chemin.read_bytes().split(b"\n", 3)
    return b"\n".join(lignes[:3]) + b"\n", lignes[3]


def main():
    entete, pixels = lire_ppm(ICI / "data" / "tux6.ppm")
    key = get_random_bytes(16)
    SORTIE.mkdir(exist_ok=True)

    # Question 1 : mode ECB
    ecb = AES.new(key, AES.MODE_ECB)
    (SORTIE / "tux_ecb.ppm").write_bytes(entete + ecb.encrypt(pad(pixels)))

    # Question 2 : mode CBC avec IV aléatoire
    cbc = AES.new(key, AES.MODE_CBC, get_random_bytes(AES.block_size))
    (SORTIE / "tux_cbc.ppm").write_bytes(entete + cbc.encrypt(pad(pixels)))

    print("Images écrites dans", SORTIE)


if __name__ == "__main__":
    main()
