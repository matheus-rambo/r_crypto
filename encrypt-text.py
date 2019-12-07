from source.r_crypto import Cryptor
import argparse
from source.arparse_util import convert_string_to_bool

parser = argparse.ArgumentParser(description='Encrypt some text.', add_help=True)

parser.add_argument('--destiny-file', '--df', type=str, help='File that the text encrypted will be stored.', dest='destiny_file')
parser.add_argument('--show', '--s', type=str, default='n', help='Show the characters that you typed.', dest='show_user_input')
parser.add_argument('--secret-key-computed', '--skc', type=str, default='n', help='If you have an secret key that was generated with your key, you can use it here.', dest='is_secret_key_computed' )

# we get the command line arguments
args = parser.parse_args() 

# the file of destiny to store the encrypted text
destiny_file = args.destiny_file

# if user want to see his inputs
show_user_input = convert_string_to_bool(args.show_user_input)

# if the user already has an computed secret key, if yes, we will ask him to input and then create
# the Fernet with his keys
is_secret_key_computed = convert_string_to_bool(args.is_secret_key_computed)

def main():
    key = None
    secret_key = None
    if show_user_input:
        key = input('Insert your key:\t')
        if is_secret_key_computed:
            secret_key = input('Insert your secret key:\t')
    else:
        from getpass import getpass
        key = getpass('Insert your key:\t')
        if is_secret_key_computed:
            secret_key = getpass('Insert your secret key:\t')
        
    cryptor = Cryptor(key, secret_key)    
    
    
    

if __name__ == "__main__":
    main()




