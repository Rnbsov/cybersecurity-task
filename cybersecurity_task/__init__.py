from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

# Функция для генерации ключа и вектора инициализации (IV)
def generate_key_iv():
    key = os.urandom(32)  # Генерация 256-битного ключа (32 байта)
    iv = os.urandom(16)   # Генерация IV (16 байт для AES)
    return key, iv

# Функция для шифрования сообщения
def encrypt_message(key, iv, message):
    # Паддинг сообщения до блока кратного 128 битам
    padder = padding.PKCS7(128).padder()
    padded_message = padder.update(message.encode()) + padder.finalize()

    # Создание шифра AES с CBC-режимом
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Шифрование сообщения
    encrypted_message = encryptor.update(padded_message) + encryptor.finalize()
    return encrypted_message

# Функция для расшифровки сообщения
def decrypt_message(key, iv, encrypted_message):
    # Создание шифра AES с CBC-режимом
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Расшифровка сообщения
    padded_message = decryptor.update(encrypted_message) + decryptor.finalize()

    # Удаление паддинга
    unpadder = padding.PKCS7(128).unpadder()
    message = unpadder.update(padded_message) + unpadder.finalize()
    return message.decode()

# Основной код для демонстрации
if __name__ == "__main__":
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
