import Cryptographer as crp


def encrypt_data(data_name):
    for i in data_name:
        crp.write_key(i)
        crp.encrypt(i, crp.load_key(i))


def decrypt_data(data_name):
    for i in data_name:
        crp.decrypt(i, crp.load_key(i))


if __name__ == "__main__":
    data_name = ['ClearData', 'PredictData', 'DataUpload', 'Models']
    encrypt_data(data_name)
