from Crypto.Cipher import AES


def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)


def unpad(s):
    return s.rstrip(b"\0")
