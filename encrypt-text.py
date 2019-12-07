from source.r_crypto import Cryptor, Keys
import argparse
from source.app_util import convert_string_to_bool, write

parser = argparse.ArgumentParser(description='Encrypt some text. For security reasons, you can not pass your text and your keys as command line arguments', add_help=True)

parser.add_argument('--destiny-file', '--df', type=str, help='File that the text encrypted will be stored.', dest='destiny_file')
parser.add_argument('--show', '--s', type=str, default='n', help='Show the characters that you typed.', dest='show_user_input')
parser.add_argument('--secret-key-computed', '--skc', type=str, default='n', help='If you have an secret key that was generated with your key, you can use it here.', dest='is_secret_key_computed' )
parser.add_argument('--keys-destiny-file', '--kdf', type=str, help='If you want to save the keys at a file. Otherwise, the keys will be prompted.', dest='keys_destiny_file')

# we get the command line arguments
args = parser.parse_args() 

# the file of destiny to store the encrypted text
destiny_file = args.destiny_file

# if user want to see his inputs
show_user_input = convert_string_to_bool(args.show_user_input)

# if the user already has an computed secret key, if yes, we will ask him to input and then create
# the Fernet with his keys
is_secret_key_computed = convert_string_to_bool(args.is_secret_key_computed)

# if the user want to save the keys at a file
keys_destiny_file = args.keys_destiny_file

def main():
    
    key = None
    secret_key = None
    message = None
    
    if show_user_input:
        key = input('Insert your key:\t')
        if is_secret_key_computed:
            secret_key = input('Insert your secret key:\t')
        message = input('Insert your message: \t')
    else:
        from getpass import getpass
        key = getpass('Insert your key:\t')
        if is_secret_key_computed:
            secret_key = getpass('Insert your secret key:\t')
        message = getpass('Insert your message: \t')

        
    # cryptor object    
    cryptor = Cryptor(key, secret_key)    
    
    # keys object
    keys = cryptor.keys
    
    # encrypted message
    encrypted_message = cryptor.encrypt(message)
    
    # user wants to save his encrypted content in a file
    if destiny_file is not None:
        write(destiny_file, encrypted_message, '.rencrypted')
    
    else:
        # just prompt
        print('Your encrypted text:\t{}'.format(encrypted_message))
        
    
    if  keys_destiny_file is not None:
        # save the keys to a file
        write(keys_destiny_file, keys.get_keys(), '.rkeys')
        
    else:
        # show the keys at the console
        keys.show_keys()
        
    
if __name__ == "__main__":
    main()




