import Cryptographer as crp


def ecnrypt_data(data_name):
    for i in data_name:
        crp.write_key(i)
        crp.encrypt(i, crp.load_key(i))


def decrypt_data(data_name):
    for i in data_name:
        crp.decrypt(i, crp.load_key(i))


if __name__ == "__main__":
    data_name = ['ClearData', 'DataForForecasting', 'DataUpload', 'Models']
    ecnrypt_data(data_name)
