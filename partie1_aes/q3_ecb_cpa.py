"""Question 3 : adversaire qui gagne le jeu CPA contre AES-ECB avec probabilité 1."""
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

BLOC = AES.block_size


def challenger(m0: bytes, m1: bytes) -> tuple[int, bytes]:
    """Tire une clé et un bit b, renvoie b et c* = Enc_k(m_b)."""
    key = get_random_bytes(16)
    b = get_random_bytes(1)[0] & 1
    return b, AES.new(key, AES.MODE_ECB).encrypt([m0, m1][b])


def adversaire():
    x, y = b"A" * BLOC, b"B" * BLOC
    m0 = x + x  # deux blocs identiques
    m1 = x + y  # deux blocs différents
    b, c = challenger(m0, m1)
    b_devine = 0 if c[:BLOC] == c[BLOC:] else 1
    return b == b_devine


if __name__ == "__main__":
    essais = 1000
    victoires = sum(adversaire() for _ in range(essais))
    print(f"L'adversaire gagne {victoires}/{essais} parties")
