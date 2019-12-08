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
optional.add_argument('--save-content', type=str, help='If you want to save the encrypted content to a file, otherwise it will be prompted at console.', dest='save_content')
optional.add_argument('--show', type=str, default='n', help='Show the characters that you typed.', dest='show_user_input')
optional.add_argument('--secret-key-computed', type=str, default='n', help='If you have an secret key that was generated with your key, you can use it here.', dest='is_secret_key_computed' )
optional.add_argument('--save-keys', type=str, help='If you want to save the keys at a file. Otherwise, the keys will be prompted.', dest='save_keys')
optional.add_argument('--buffer-size', type=int, default=2048, help='Size of the buffer when reading data of a file', dest='buffer_size')


# we get the command line arguments
args = parser.parse_args() 

# if user wants to save the encrypted content
save_content = args.save_content

# if user want to see his inputs
show_user_input = convert_string_to_bool(args.show_user_input)

# if the user already has an computed secret key, if yes, we will ask him to input and then create
# the Fernet with his keys
is_secret_key_computed = convert_string_to_bool(args.is_secret_key_computed)

# if the user want to save the keys at a file
save_keys = args.save_keys

# if the users wants to encrypt a file
is_file = convert_string_to_bool(args.is_file)

# Size of buffer for reading characters of a text file
buffer_size = args.buffer_size

def main():
    
    # user key
    key = None
    
    # secret key generated
    secret_key = None
    
    # messages that will be encrypt
    messages = []
        
    if show_user_input:
        
        key = input('Insert your key:\t')
        if is_secret_key_computed:
            secret_key = input('Insert your secret key:\t')
        
        # if the user wants to encrypt a file 
        if is_file:
            # we read the file name and then read its content
            print('For two or more files, type: file1 file2 file3 . . .')
            files_string = input('Insert the path of the files: \t')        
            
            files = files_string.split(' ')
            
            for file_name in files:
                # reads the content of a file
                messages.append(read_file_content(file_name, buffer_size))
            
        else:
            # user want to encrypt a text message
            messages.append(input('Insert your message: \t'))
    
    else:
        from getpass import getpass
        key = getpass('Insert your key:\t')
        
        if is_secret_key_computed:
            secret_key = getpass('Insert your secret key:\t')
            
        if is_file:
            # we read the file name and then read its content
            print('For two or more files, type: file1 file2 file3 . . .')
            files_string = input('Insert the path of the files: \t')        

            # splits multiple files            
            files = files_string.split(' ')
            
            for file_name in files:
                messages.append(read_file_content(file_name, buffer_size))
        else:
            messages.append(getpass('Insert your message: \t'))

        
    # cryptor object    
    cryptor = Cryptor(key, secret_key)    
    
    # keys object
    keys = cryptor.keys
    
    for message in messages:
        
        # encrypted message
        encrypted_message = cryptor.encrypt(message)
        
        # user wants to save his encrypted content in a file
        if save_content:
            destiny_file = None
        
            if show_user_input:
                destiny_file = input('Insert the name of encrypted file: \t')
            else:
                from getpass import getpass
                destiny_file = getpass('Insert the name of encrypted file: \t')
        
            write(destiny_file, encrypted_message, '.rencrypted')
        
        else:
            # just prompt
            print('Your encrypted text:\t{}'.format(encrypted_message))
            
        
        
    if  save_keys is not None:
        # save the keys to a file
        keys_destiny_file = None
        
        if show_user_input:
            keys_destiny_file = input('Insert the name of keys file: \t')
        else:
            from getpass import getpass
            keys_destiny_file = getpass('Insert the name of keys file: \t')        
        
        write(keys_destiny_file, keys.get_keys(), '.rkeys')
            
    else:
        # show the keys at the console
        keys.show_keys()



        
    
if __name__ == "__main__":
    main()




