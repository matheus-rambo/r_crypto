#!/usr/bin/python

import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import random
import time

class Keys():
    def __init__(self, user_key:str, secret_key:str = None):
        self.user_key = user_key
        # When decrypt the user already has the secret key
        self.secret_key = if secret_key is None self.generate_custom_key() else secret_key
    
    def generate_secret_key(self):
        hexadecimal_key = self.user_key.hex()
        for integer in range(20):
            hexadecimal_key = hexadecimal_key + str(random.randint(1000, 10000)).hex()
        hexadecimal_key = self.user_key.hex() + hexadecimal_key + str(time.time()).hex()
        return hexadecimal_key

    def save_to_file(self, file_name:str):
        pass


class Cryptor():
    def __init__(self, user_key:str, secret_key:str = None, charset:str = 'utf-8'):
        self.keys = Keys(user_key, secret_key)
        self.charset = charset
        self._fernet = self.generate_fernet()
    
    def generate_fernet(self):
        kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=bytes(self.keys.secret_key.encode(utf_8_unicode)),
        iterations=100000,
        backend=default_backend()
        )
        fernet_key = base64.urlsafe_b64encode(kdf.derive(keys.user_key.encode(utf_8_unicode)))
        return Fernet(fernet_key)    
                
    def encrypt(self, content:str):
        return self._fernet.encrypt(content.encode(self.charset))
    
    def decrypt(self, content:str):
        try:
            return self._fernet.decrypt(content.decode(self.charset))
        except Exception:
            from .RCrypto import InvalidKeyException
            raise InvalidKeyException()
    

