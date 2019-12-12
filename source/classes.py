#!/usr/bin/python

import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import random
import time

class Keys():
    def __init__(self, user_key:str, secret_key:str = None, charset:str = 'utf-8'):
        self.user_key = user_key
        self.charset = charset
        self.secret_key = self.generate_secret_key() if secret_key is None else secret_key

    def __del__(self):
        pass

    def generate_secret_key(self):
        hexadecimal_key = self.user_key.encode(self.charset).hex()
        for integer in range(20):
            hexadecimal_key = hexadecimal_key + str(random.randint(1000, 10000)).encode(self.charset).hex()
        hexadecimal_key = self.user_key.encode(self.charset).hex() + hexadecimal_key + str(time.time()).encode(self.charset).hex()
        print('\nSecret key was generated.')
        return hexadecimal_key

    def show_keys(self):
        print('\nYour key is:\t{}'.format(self.user_key))
        print('Your secret key is:\t{}'.format(self.secret_key))

    def get_keys(self):
        from json import dumps
        json = {
            "key": self.user_key,
            "secret_key": self.secret_key
        }
        return dumps(json)        
        

class InvalidKeyException(Exception):
    def __init__(self):
        self.message = "\n\nWe could not decrypt your content! Are you using the correct key and the correct Secret Key?"
        super(InvalidKeyException, self).__init__(self.message)

class Cryptor():
    # Constructor
    def __init__(self, user_key:str, secret_key:str = None, charset:str = 'utf-8'):
        self.keys = Keys(user_key, secret_key)
        self.charset = charset
        self._fernet = self.generate_fernet()

    # Destructor
    def __del__(self):
        del self._fernet
        del self.keys
    
    
    def generate_fernet(self):
        secret_key = self.keys.secret_key
        key = self.keys.user_key
        kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=bytes(secret_key.encode(self.charset)),
        iterations=100000,
        backend=default_backend()
        )
        fernet_key = base64.urlsafe_b64encode(kdf.derive(key.encode(self.charset)))        
        return Fernet(fernet_key)    
                
    def encrypt(self, content:str):
        return self._fernet.encrypt(content.encode(self.charset)).decode(self.charset)
    
    def decrypt(self, content:str):
        try:
            return self._fernet.decrypt(content.decode(self.charset))
        except Exception:
            raise InvalidKeyException()
    
