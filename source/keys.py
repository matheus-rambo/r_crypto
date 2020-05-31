from json    import dumps
from secrets import token_urlsafe, choice
from string  import ascii_letters, digits

class Keys():

    def __init__(self, secret_key:str, salt:str = None, charset:str = 'utf-8'):
        self.secret_key       = secret_key
        self.charset          = charset
        self.salt             = self._generate_salt() if salt is None else salt
       
    def __del__(self):
        pass

    def _generate_salt(self):
        
        alphabet        = ascii_letters + digits
        token           = token_urlsafe(32)
        salt      = ""
        secret_key_size = 25
        # generate a password with 50 characters
        while secret_key_size > 0:            
            if secret_key_size % 4 == 0:
                salt = choice(alphabet) + salt + choice(token)                
            elif secret_key_size % 3 == 0:
                salt = choice(token) + salt + choice(alphabet)                 
            elif secret_key_size % 2 == 0:
                salt = salt + choice(alphabet) + choice(token)
            else:
                salt = salt + choice(token) + choice(alphabet)
            secret_key_size -= 1

        return salt      

    def get_keys(self) -> str:
        return {
            'secret_key': self.secret_key, 
            'salt': self.salt
        }

    def get_keys_as_json(self) -> str:
        dictionary = self.get_keys()
        return dumps(dictionary)