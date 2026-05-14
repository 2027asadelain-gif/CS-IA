from crypto_utils import derive_shared_key, encrypt_message, decrypt_message


def main():
    key = derive_shared_key()

    user_input = input("Type a message: ")

    nonce, ciphertext = encrypt_message(user_input, key)
    decrypted = decrypt_message(nonce, ciphertext, key)

    print("\n--- Results ---")
    print("Original message:", user_input)
    print("Nonce (hex):", nonce.hex())
    print("Ciphertext (hex):", ciphertext.hex())
    print("Decrypted message:", decrypted)


if __name__ == "__main__":
    main()