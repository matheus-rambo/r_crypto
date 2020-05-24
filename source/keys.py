from json    import dumps
from secrets import token_urlsafe, choice
from string  import ascii_letters, digits

class Keys():

    def __init__(self, user_key:str, secret_key:str = None, charset:str = 'utf-8'):
        self.user_key         = user_key
        self.charset          = charset
        self.secret_key       = self.generate_secret_key() if secret_key is None else secret_key
       
    def __del__(self):
        pass

    def generate_secret_key(self):
        
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

    def get_keys(self) -> str:
        return {
            'key': self.user_key, 
            'secret_key': self.secret_key
        }

    def get_keys_as_json(self) -> str:
        dictionary = self.get_keys()
        return dumps(dictionary)