from cryptography.fernet                       import Fernet
from cryptography.hazmat.backends              import default_backend
from cryptography.hazmat.primitives            import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
from source.keys import Keys


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
        return self._fernet.decrypt(content)
