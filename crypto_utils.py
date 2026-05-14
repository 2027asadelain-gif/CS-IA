from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
import os


def derive_shared_key():
    private_key_a = X25519PrivateKey.generate()
    public_key_a = private_key_a.public_key()

    private_key_b = X25519PrivateKey.generate()
    public_key_b = private_key_b.public_key()

    shared_secret_a = private_key_a.exchange(public_key_b)
    shared_secret_b = private_key_b.exchange(public_key_a)

    if shared_secret_a != shared_secret_b:
        raise ValueError("Shared secrets do not match.")

    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b"cabal messaging session key",
    ).derive(shared_secret_a)

    return derived_key

def encrypt_message(message: str, key: bytes):
    chacha = ChaCha20Poly1305(key)
    nonce = os.urandom(12)
    plaintext = message.encode("utf-8")
    ciphertext = chacha.encrypt(nonce, plaintext, None)
    return nonce, ciphertext


def decrypt_message(nonce: bytes, ciphertext: bytes, key: bytes):
    chacha = ChaCha20Poly1305(key)
    plaintext = chacha.decrypt(nonce, ciphertext, None)
    return plaintext.decode("utf-8")