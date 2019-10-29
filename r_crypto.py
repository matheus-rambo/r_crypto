import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import random

def generate_custom_key(password:str):
    custom_key = ""
    for integer in range(20):
        custom_key = custom_key + convert_to_hex(str(random.randint(1000, 10000)))
    custom_key = convert_to_hex(password) + custom_key
    print("Warning!!!\nYou must store the salt in a trusted location!\nSalt Key is: ", custom_key)
    kdf = PBKDF2HMAC(
     algorithm=hashes.SHA256(),
     length=32,
     salt=bytes(custom_key.encode("utf-8")),
     iterations=100000,
     backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode("utf-8")))
    return Fernet(key)

def generate_key(password:str, decoded_salt:str):
    kdf = PBKDF2HMAC(
     algorithm=hashes.SHA256(),
     length=32,
     salt=bytes(decoded_salt.encode()),
     iterations=100000,
     backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(bytes(password.encode())))
    return Fernet(key)

def encrypt(fernet:Fernet, content:str):
    return fernet.encrypt(content.encode())

def decrypt(fernet:Fernet, content:str):
    return (fernet.decrypt(content.encode()))

def convert_to_hex(key:str):
    return key.encode('utf-8').hex()

