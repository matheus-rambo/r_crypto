#!/usr/bin/python

import base64
import random
import time
from cryptography.fernet                       import Fernet
from cryptography.hazmat.backends              import default_backend
from cryptography.hazmat.primitives            import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class Keys():
    def __init__(self, user_key:str, secret_key:str = None, charset:str = 'utf-8'):
        self.user_key         = user_key
        self.charset          = charset
        self.secret_key       = self.generate_secret_key() if secret_key is None else secret_key
       
    def __del__(self):
        pass

    def generate_secret_key(self):
        from secrets import token_urlsafe, choice
        from string  import ascii_letters, digits
        
        alphabet        = ascii_letters + digits
        token           = token_urlsafe(32)
        secret_key      = ""
        secret_key_size = 25
        # generate a password with 50 characters
        while secret_key_size > 0:            
            if secret_key_size % 4 == 0:
                secret_key = choice(alphabet) + secret_key + choice(token)                
            elif secret_key_size % 3 == 0:
                secret_key = choice(token) + secret_key + choice(alphabet)                 
            elif secret_key_size % 2 == 0:
                secret_key = secret_key + choice(alphabet) + choice(token)
            else:
                secret_key = secret_key + choice(token) + choice(alphabet)
            secret_key_size -= 1

        return secret_key


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
        self.update_keys(user_key, secret_key, charset)

    # Destructor
    def __del__(self):
        del self._fernet
        del self.keys
    
    def update_keys(self, user_key: str, secret_key:str = None, charset:str = 'utf-8'):
        self.keys = Keys(user_key, secret_key)
        self.charset = charset
        self._fernet = self.generate_fernet()

    
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
            return self._fernet.decrypt(content.encode(self.charset)).decode(self.charset)
        except Exception:
            raise InvalidKeyException()
    
