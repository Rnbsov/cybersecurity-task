from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

def generate_key_iv():
    key = os.urandom(32)
    iv = os.urandom(16) 
    return key, iv

def encrypt_message(key, iv, message):
    padder = padding.PKCS7(128).padder()
    padded_message = padder.update(message.encode()) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    encrypted_message = encryptor.update(padded_message) + encryptor.finalize()
    return encrypted_message

def decrypt_message(key, iv, encrypted_message):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    padded_message = decryptor.update(encrypted_message) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    message = unpadder.update(padded_message) + unpadder.finalize()
    return message.decode()

if __name__ == "__main__":
    key, iv = generate_key_iv()

    original_message = "Это тестовое сообщение."
    print(f"Оригинальное сообщение: {original_message}")

    encrypted_message = encrypt_message(key, iv, original_message)
    print(f"Зашифрованное сообщение (в байтах): {encrypted_message}")

    decrypted_message = decrypt_message(key, iv, encrypted_message)
    print(f"Расшифрованное сообщение: {decrypted_message}")
