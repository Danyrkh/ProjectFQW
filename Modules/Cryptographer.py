from cryptography.fernet import Fernet
import os


def write_key(name):
    key = Fernet.generate_key()
    if not os.path.isdir("/Users/hamster/Desktop/ВКР/Keys"):
        os.mkdir("/Users/hamster/Desktop/ВКР/Keys")
    with open(f'/Users/hamster/Desktop/ВКР/Keys/{name}.key', 'wb') as key_file:
        key_file.write(key)


def load_key(name):
    return open(f'/Users/hamster/Desktop/ВКР/Keys/{name}.key', 'rb').read()


def encrypt(filename, key):
    f = Fernet(key)
    with open(f'/Users/hamster/Desktop/ProjectFQW/Excel Files/{filename}.xlsx', 'rb') as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(f'/Users/hamster/Desktop/ProjectFQW/Excel Files/{filename}.xlsx', 'wb') as file:
        file.write(encrypted_data)


def decrypt(filename, key):
    f = Fernet(key)
    with open(f'/Users/hamster/Desktop/ProjectFQW/Excel Files/{filename}.xlsx', 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(f'/Users/hamster/Desktop/ProjectFQW/Excel Files/{filename}.xlsx', 'wb') as file:
        file.write(decrypted_data)
    os.remove(f'/Users/hamster/Desktop/ВКР/Keys/{filename}.key')
    if len(os.listdir("/Users/hamster/Desktop/ВКР/Keys")) == 0:
        os.rmdir("/Users/hamster/Desktop/ВКР/Keys")


if __name__ == "__main__":
    write_key('default_crypto_key')
