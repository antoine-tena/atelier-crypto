"""Bourrage par octets nuls (préambule du TP)."""
from Crypto.Cipher import AES


def pad(s: bytes) -> bytes:
    """Ajoute des octets nuls jusqu'à obtenir un multiple de la taille de bloc."""
    return s + b"\x00" * (AES.block_size - len(s) % AES.block_size)


def unpad(s: bytes) -> bytes:
    """Supprime les octets nuls terminaux."""
    return s.rstrip(b"\x00")
