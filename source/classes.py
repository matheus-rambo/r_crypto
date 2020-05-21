#!/usr/bin/python

import base64
import random
import time
from cryptography.fernet                       import Fernet
from cryptography.hazmat.backends              import default_backend
from cryptography.hazmat.primitives            import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from getpass                                   import getpass
from enum                                      import Enum


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
    def __init__(self, keys: Keys, charset:str = 'utf-8'):
        self.keys    = keys
        self.charset = charset
        self._fernet = None
        self.update_keys(keys, charset)

    # Destructor
    def __del__(self):
        del self._fernet
        del self.keys
    
    def update_keys(self, keys:Keys, charset:str = 'utf-8'):
        self.keys    = keys
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
                
    def encrypt(self, content:bytes):  
        return self._fernet.encrypt(content)
    
    def decrypt(self, content:bytes):
        try:
            return self._fernet.decrypt(content)
        except Exception:
            raise InvalidKeyException()




class ContentType(Enum):
    TEXT      = ('text')
    FILE      = ('file')
    DIRECTORY = ('directory')

    def __init__(self, type_str:str):
        self._type = type_str
        

class Encrypted():
    def __init__(self):
        self.message      = None
        self.info         = None
        self.filename     = None
        self.created_by   = None
        self.created_date = None
        self.user_message = None

    def extract_metadata(self):
        if self.info:
            info_str = self.info.decode('utf-8').split(';\0;')
            if len(info_str) == 4:
                self.filename = info_str[3]
            self.created_date = info_str[0]
            self.created_by   = info_str[1]
            self.user_message = info_str[2]
    

class File():
    def __init__(self, filename:str, charset: str = 'utf-8', chunk_size:int = None):
        self.filename   = filename
        self.chunk_size = chunk_size
        self.charset    = charset

    def read_content(self):
        byte_array = bytearray()
        buffer     = None
        with open(file = self.filename, mode = 'rb') as file:        
            while True:
                buffer = file.read(self.chunk_size)
                if buffer:
                    for byte in buffer:
                        byte_array.append(byte)
                else:
                    break
        return bytes(byte_array)

    def read_content_to_json(self):
        content = self.read_content()
        from json import loads
        return loads(content.decode(self.charset))
    
    def write(self, content:bytes):
        with open(file = self.filename, mode = 'wb') as file:
            file.write(content)


class IOUtil():
    def __init__(self, show_input:bool):
        self.show_input = show_input

    def stdin(self, message:str):
        if self.show_input:
            return input(message)
        return getpass(message)

    def read_ask_answear(self, message:str, acceptable_answear:chr):
        answear = self.stdin(message)
        return False if ( answear is None or answear.strip() == '' ) else answear.lower()[0] == acceptable_answear

    def stdout(self, message:str, parameters:dict = None):
        if parameters is not None:
            print(message.format(**parameters))
        else:
            print(message)

class Cryptography():

    def __init__(self, use:str, encryption:bool, save_content:bool, show_input:bool, 
            secret_key_computed:bool, save_keys:bool, chunk_size:int, read_keys_file:bool, charset:str, send_email:bool):

        # Objects that will be used in the internally objects
        self._content_type = ContentType(use)
        self._encryption = encryption
        self._save_content  = save_content
        self._save_keys     = save_keys     
        self._chunk_size   = chunk_size
        self._charset = charset
        self._send_email = send_email

        # Objects that are used internally
        self._io   = IOUtil(show_input)
        self._keys = self.construct_keys(read_keys_file = read_keys_file, secret_key_computed = secret_key_computed)



    def construct_keys(self, read_keys_file:bool, secret_key_computed:bool):

        # User passphrase
        user_key   = None

        # if the secret key remains none, a key will be generated
        secret_key = None

        # The user wants to read the keys from a file
        if read_keys_file:
            filename = self._io.stdin("Insert the name of yours keys file:\t")
            file_object = File(filename, self._charset, self._chunk_size)   
            json_bytes = file_object.read_content_to_json()
            del file_object
            user_key   = json_bytes['key']
            secret_key = json_bytes['secret_key']
        else:
            user_key = self._io.stdin("Insert your key:\t")
            # The user already has a secret key or he is decrypting something
            if secret_key_computed or not self._encryption:
                secret_key = self._io.stdin("Insert your secret key:\t")

        ## Construc the keys object
        return Keys(user_key=user_key, secret_key=secret_key)

