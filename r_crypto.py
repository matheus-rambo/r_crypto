import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import random

def generateCustomKey(password:str):
    custom_key = convertToHex(password)
    for integer in range(20):
        custom_key = custom_key + str(random.randint(1, 1000))
    #salt = os.urandom(16)
    encoded_password = (password + custom_key) 
    print("Warning!!!\nYou must store the salt in a trusted location!\nSalt Key is: ", encoded_password)
    kdf = PBKDF2HMAC(
     algorithm=hashes.SHA256(),
     length=32,
     salt=bytes(encoded_password.encode()),
     iterations=100000,
     backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return Fernet(key)

def generateKey(password:str, decoded_salt:str):
    kdf = PBKDF2HMAC(
     algorithm=hashes.SHA256(),
     length=32,
     salt=bytes(decoded_salt.encode()),
     iterations=100000,
     backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return Fernet(key)

def encrypt(fernet:Fernet, content:str):
    return fernet.encrypt(content.encode())

def decrypt(fernet:Fernet, content:str):
    return (fernet.decrypt(content.encode()))

def convertToHex(key:str):
    return key.hex()

