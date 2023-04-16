from cryptography.fernet import Fernet


def write_key(name):
    key = Fernet.generate_key()
    with open(f'{name}.key', 'wb') as key_file:
        key_file.write(key)


def load_key(name):
    return open(f'{name}.key', 'rb').read()


def encrypt(filename, key):
    f = Fernet(key)
    with open(f'{filename}.xlsx', 'rb') as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(f'{filename}.xlsx', 'wb') as file:
        file.write(encrypted_data)


def decrypt(filename, key):
    f = Fernet(key)
    with open(f'{filename}.xlsx', 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(f'{filename}.xlsx', 'wb') as file:
        file.write(decrypted_data)


if __name__ == "__main__":
    write_key('default_crypto_key')
