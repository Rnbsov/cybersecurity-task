from . import generate_key_iv, encrypt_message, decrypt_message

def main():
    # Генерация ключа и IV
    key, iv = generate_key_iv()

    # Оригинальное сообщение
    original_message = "Это тестовое сообщение."
    print(f"Оригинальное сообщение: {original_message}")

    # Шифрование
    encrypted_message = encrypt_message(key, iv, original_message)
    print(f"Зашифрованное сообщение (в байтах): {encrypted_message}")

    # Расшифровка
    decrypted_message = decrypt_message(key, iv, encrypted_message)
    print(f"Расшифрованное сообщение: {decrypted_message}")

if __name__ == "__main__":
    main()