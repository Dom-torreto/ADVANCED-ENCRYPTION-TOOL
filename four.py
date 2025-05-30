import os
import sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes, padding
from cryptography.hazmat.backends import default_backend
from getpass import getpass

def generate_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # AES-256 = 32 bytes = 256 bits
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def encrypt_file(password: str, input_path: str, output_path: str):
    salt = os.urandom(16)
    iv = os.urandom(16)
    key = generate_key(password, salt)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()

    with open(input_path, 'rb') as f:
        data = f.read()

    padded_data = padder.update(data) + padder.finalize()
    encrypted = encryptor.update(padded_data) + encryptor.finalize()

    with open(output_path, 'wb') as f:
        f.write(salt + iv + encrypted)

    print("✅ File encrypted successfully!")

def decrypt_file(password: str, input_path: str, output_path: str):
    with open(input_path, 'rb') as f:
        salt = f.read(16)
        iv = f.read(16)
        encrypted = f.read()

    key = generate_key(password, salt)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    unpadder = padding.PKCS7(128).unpadder()

    decrypted_padded = decryptor.update(encrypted) + decryptor.finalize()
    decrypted = unpadder.update(decrypted_padded) + unpadder.finalize()

    with open(output_path, 'wb') as f:
        f.write(decrypted)

    print("✅ File decrypted successfully!")

def main():
    print("=== AES-256 FILE ENCRYPTION TOOL ===")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ").strip()

    if choice not in ['1', '2']:
        print("Exiting...")
        sys.exit()

    input_file = input("Enter input file path: ").strip()
    output_file = input("Enter output file path: ").strip()
    password = getpass("Enter password: ")

    try:
        if choice == '1':
            encrypt_file(password, input_file, output_file)
        elif choice == '2':
            decrypt_file(password, input_file, output_file)
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    main()
