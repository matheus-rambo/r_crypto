#!/usr/bin/python

import base64
import random
import time
from cryptography.fernet                       import Fernet
from cryptography.hazmat.backends              import default_backend
from cryptography.hazmat.primitives            import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from getpass                                   import getpass, getuser
from enum                                      import Enum
from source.app_util                           import persist_info
from json                                      import dumps, loads
from datetime import datetime

_NULL_BYTES   = '\0\0\0'
_WRITE_BINARY = 'wb'
_READ_BINARY  = 'rb'

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
        

class Message():

    def __init__(self, content:bytes, user_message:str, file_path:str = None):

        self.content      = content
        self.user_message = user_message
        self.filename     = self._get_filename(file_path) if file_path is not None else None 
        self.created_by   = getuser()
        self.created_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.file_path    = file_path
    
    def _metadata_to_json(self, charset:str = 'utf-8') -> str:

        metadata = {
            "filename"    : self.filename,
            "created_by"  : self.created_by,
            "created_date": self.created_date,
            "user_message": self.user_message,
            "file_path"   : self.file_path
        }  

        json_str = dumps(metadata)
        return json_str

    def compact(self, charset:str) -> bytes:

        json_bytes = self._to_json_bytes.encode(charset)

        # init the array with 3 null bytes
        array_bytes = bytearray(bytes(_NULL_BYTES))

        # copy the metadata
        for byte in json_bytes:
            array_bytes.appen(byte)
        
        # insert three null bytes
        array_bytes.append(0)
        array_bytes.append(0)
        array_bytes.append(0)

        # copy the content
        for byte in self.content:
            array_bytes.append(byte)

        # creates a new byte array
        return bytes(array_bytes)

    @staticmethod
    def create_from_json(json_str:str):
        pass

    def _get_filename(self, path:str):
        if '/' in path:
            return path[path.rindex('/') + 1:] 
        elif '\\' in path:
            return path[path.rindex('\\') + 1:] 
        else:
            return path

class File():
    def __init__(self, filename:str, charset: str = 'utf-8', chunk_size:int = None):
        self.filename   = filename
        self.chunk_size = chunk_size
        self.charset    = charset

    def read(self):
        byte_array = bytearray()
        buffer     = None
        with open(file = self.filename, mode = _READ_BINARY ) as file:        
            while True:
                buffer = file.read(self.chunk_size)
                if buffer:
                    for byte in buffer:
                        byte_array.append(byte)
                else:
                    break
        return bytes(byte_array)

    def read_content_to_json(self):
        content = self.read()
        from json import loads
        return loads(content.decode(self.charset))
    
    def write(self, content:bytes):
        with open(file = self.filename, mode = _WRITE_BINARY ) as file:
            file.write(content)


class IOUtil():
    def __init__(self, show_input:bool):
        self.show_input = show_input

    def stdin(self, message:str):
        if self.show_input:
            return input(message)
        return getpass(message)

    def stdin_to_bytes(self, message:str, charset:str = 'utf-8'):
        return self.stdin(message).encode(charset)

    def read_ask_answear(self, message:str, acceptable_answear:chr = 'y'):
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
        self._encryption   = encryption
        self._save_content = save_content
        self._save_keys    = save_keys     
        self._chunk_size   = chunk_size
        self._charset      = charset
        self._send_email   = send_email

        # Objects that are used internally
        self._io       = IOUtil(show_input)
        self._keys     = self._construct_keys(read_keys_file = read_keys_file, secret_key_computed = secret_key_computed)
        self._crypto   = None
        self._messages = None


    def _construct_keys(self, read_keys_file:bool, secret_key_computed:bool) -> Keys:

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

    def _read(self) -> None:

        if self._content_type == ContentType.TEXT:

            self._messages = []
            self._messages.append(self._read_text())

        elif self._content_type == ContentType.FILE:
            
            self._messages = self._read_file()

        else:
            # directory
            pass
        


    def _read_text(self) -> Message:

        message      = None
        user_message = None

        if self._encryption:
            message = self._io.stdin_to_bytes('Insert the message: \t', self._charset)
            insert_message_inside = self._io.read_ask_answear('Do you want to store a message inside the encrypted file? [Yes, No]:')
            if insert_message_inside:
                user_message = self._io.stdin("Insert the message to store inside: ")
        else:
            message = self._io.stdin_to_bytes('Insert the message: \t', self._charset)

        return Message(content=message, user_message=user_message)
    
    def _read_file(self) -> []:

        messages = []
        self._io.stdout("For two or more files, type: file;file;file3")
        files = self._io.stdin("Files: \t ").split(";")

        for filename in files:
            messages.append(self._read_file_content(filename))
        return messages
        

    def _read_file_content(self, filename:str) -> Message:
        
        user_message = None

        if self._encryption:
            insert_message_inside = self._io.read_ask_answear('Do you want to store a message inside the encrypted file? [Yes, No]:')
          
            if insert_message_inside:
                user_message = self._io.stdin("Insert the message to store inside: ")
        
        file_object = File(filename=filename, charset=self._charset, chunk_size=self._chunk_size)
        message = file_object.read()
        del file_object
        return Message(content=message, user_message=user_message, file_path=filename)

    def _encrypt_message(self) -> None:
        self._crypto = Cryptor(self._keys, self._charset)
        for message in self._messages:
            message.content = self._crypto.encrypt(message.content)

    def init(self):
        self._read()
        if self._encryption:
            self._encrypt_message()
        else:
            pass

