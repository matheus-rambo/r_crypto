from source.r_crypto import Cryptor, Keys
import argparse
from source.app_util import convert_string_to_bool, write, read_file_content

parser = argparse.ArgumentParser(description='Encrypt text and files with this script')

parser._action_groups.pop()

required = parser.add_argument_group('required arguments')
optional = parser.add_argument_group('optional arguments')

# required arguments
required.add_argument('-is-file', type=str, help='If you want to encrypt a file, otherwise a text will be encrypted', required=True, dest='is_file')


# optional arguments
optional.add_argument('--destiny-file', type=str, help='File that the text encrypted will be stored.', dest='destiny_file')
optional.add_argument('--show', type=str, default='n', help='Show the characters that you typed.', dest='show_user_input')
optional.add_argument('--secret-key-computed', type=str, default='n', help='If you have an secret key that was generated with your key, you can use it here.', dest='is_secret_key_computed' )
optional.add_argument('--keys-destiny-file', type=str, help='If you want to save the keys at a file. Otherwise, the keys will be prompted.', dest='keys_destiny_file')
optional.add_argument('--buffer-size', type=int, default=2048, help='Size of the buffer when reading data of a file', dest='buffer_size')


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

# if the users wants to encrypt a file
is_file = convert_string_to_bool(args.is_file)

# Size of buffer for reading characters of a text file
buffer_size = args.buffer_size

def main():
    
    # user key
    key = None
    
    # secret key generated
    secret_key = None
    
    # message that will be encrypted
    message = None
    
    if show_user_input:
        
        key = input('Insert your key:\t')
        if is_secret_key_computed:
            secret_key = input('Insert your secret key:\t')
        
        # if the user wants to encrypt a file 
        if is_file:
            # we read the file name and then read its content
            file_name = input('Insert the path of the file: \t')        
            
            # reads the content of the file
            message = read_file_content(file_name, buffer_size)
            
        else:
            # user want to encrypt a text message
            message = input('Insert your message: \t')
    
    else:
        from getpass import getpass
        key = getpass('Insert your key:\t')
        
        if is_secret_key_computed:
            secret_key = getpass('Insert your secret key:\t')
            
        if is_file:
            file_name = getpass('Insert the path of the file: \t')        
            message = read_file_content(file_name, buffer_size)
        else:
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




