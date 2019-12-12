from source.r_crypto import Cryptor, Keys
import argparse
from source.app_util import write, read_file_content
from getpass import getpass


parser = argparse.ArgumentParser(description='Encrypt/Decrypt text and text files with this script. With this tool, you can encrypt/decrypt files, and texts, then save them, load file of keys and creates keys file.')

parser._action_groups.pop()

required = parser.add_argument_group('required arguments')
optional = parser.add_argument_group('optional arguments')

# required arguments
required.add_argument('-is-file', type=int, choices=[1,0], help='If you want to work over a file, otherwise a text will be used', required=True, dest='is_file')
required.add_argument('-is-encryption', type=int, choices=[1,0], help='If you want to encrypt a file, otherwise we will decrypt', required=True, dest='is_encryption')



# optional arguments
optional.add_argument('--save-content', type=int, choices=[1, 0], default=0,  help='If you want to save the encrypted content to a file, otherwise it will be prompted at console.', dest='save_content')
optional.add_argument('--show', type=int, choices=[1, 0], default=0, help='Show the characters that you typed.', dest='show_user_input')
optional.add_argument('--secret-key-computed', type=int, choices=[1,0], default=0, help='If you have an secret key that was generated with your key, you can use it here.', dest='is_secret_key_computed' )
optional.add_argument('--save-keys', type=int, choices=[1,0], default=0, help='If you want to save the keys at a file. Otherwise, the keys will be prompted.', dest='save_keys')
optional.add_argument('--buffer-size', type=int, default=2048, help='Size of the buffer when reading data from a file.', dest='buffer_size')
optional.add_argument('--read-keys-file', type=int, choices=[1, 0], default=0, help='If you have a keys file, you can read it.', dest='read_keys_file')



# we get the command line arguments
args = parser.parse_args() 

# if user wants to save the encrypted content
save_content = args.save_content

# if user want to see his inputs
show_user_input = args.show_user_input

# if the user already has an computed secret key, if yes, we will ask him to input and then create
# the Fernet with his keys
is_secret_key_computed = args.is_secret_key_computed

# if the user want to save the keys at a file
save_keys = args.save_keys

# if the users wants to encrypt a file
is_file = args.is_file

# if user wants to encrypt
is_encryption = args.is_encryption

# Size of buffer for reading characters of a text file
buffer_size = args.buffer_size

# if the user wants to read the keys from a file
read_keys_file = args.read_keys_file

def main():      


    # user key
    key = None  
    
    # secret key generated
    secret_key = None
    
    # messages that will be encrypt
    messages = []
        
    print('\n\tInit keys process . . .')     
        
    if show_user_input:
        
        # if user wants to read his keys from a file
        if read_keys_file:
            keys_file = input("Input your keys file:\t")
            keys_content = read_file_content(keys_file, buffer_size)
            from json import loads
            key = loads(keys_content)['key']
            secret_key = loads(keys_content)['secret_key']
            print('\nKeys were loaded')     
        
        else:
            key = input('Insert your key:\t')
            if is_secret_key_computed:
                secret_key = input('Insert your secret key:\t')
        
        print('\n\tInit read content process . . .')
        
        # if the user wants to encrypt a file 
        if is_file:
            # we read the file name and then read its content
            print('\nFor two or more files, type: file1 file2 file3 . . .')
            files_string = input('Insert the path of the files: \t')        
            
            files = files_string.split(' ')
            
            for file_name in files:
                # reads the content of a file
                messages.append(read_file_content(file_name, buffer_size))
            
        else:
            # user wants to encrypt a text message
            name = None
            if is_encryption:
                name = "message"
            else:
                name = "encrypted message"    

            messages.append(input('Insert the {}: \t'.format(name)))
    
    else:

        # if user wants to read his keys from a file
        if read_keys_file:
            keys_file = getpass("Input your keys file:\t")
            keys_content = read_file_content(keys_file, buffer_size)
            from json import loads
            key = loads(keys_content)['key']
            secret_key = loads(keys_content)['secret_key']
            print('\nKeys were loaded')     
        
        else:
            key = getpass('Insert your key:\t')
            if is_secret_key_computed:
                secret_key = getpass('Insert your secret key:\t')

            
        if is_file:
            # we read the file name and then read its content
            print('\nFor two or more files, type: file1 file2 file3 . . .')
            files_string = getpass('Insert the path of the files: \t')        

            # splits multiple files            
            files = files_string.split(' ')
            
            for file_name in files:
                messages.append(read_file_content(file_name, buffer_size))
        else:
            # user wants to encrypt a text message
            name = None
            if is_encryption:
                name = "message"
            else:
                name = "encrypted message"    
                
            messages.append(getpass('Insert the {}: \t'.format(name)))

    if is_encryption:
        print('\n\tInit encryption process . . .')
    else:
        print('\n\tInit decryption process . . .')
   

    # cryptor object    
    cryptor = Cryptor(key, secret_key)    
    
    # keys object
    keys = cryptor.keys
    
    file_extension = None

    if save_content and is_encryption:
        file_extension = '.rencrypted'
    elif save_content and not is_encryption:
        file_extension = '.rdecrypted'


    for message in messages:
        
        # encrypted message
        encrypted_message = cryptor.encrypt(message)
        
        # user wants to save his encrypted content in a file
        if save_content:
            print('\n\tInit save content to a file process . . .')
            destiny_file = None
        
            if is_encryption:
                if show_user_input:
                    destiny_file = input('Insert the name of encrypted file: \t')
                else:
                    destiny_file = getpass('Insert the name of encrypted file: \t')

            else:
                if show_user_input:
                    destiny_file = input('Insert the name of decrypted file: \t')
                else:
                    destiny_file = getpass('Insert the name of decrypted file: \t')

            
            write(destiny_file, encrypted_message, file_extension)
            print("\nFile created: {}".format(destiny_file + file_extension))
        
        
        else:

            if is_encryption:
                print('Your encrypted text:\t{}'.format(encrypted_message))
            else:
                print('Your decrypted text:\t{}'.format(encrypted_message))
            
        
    if save_keys:
        
        print('\n\tInit save keys to a file process . . .')
        
        # save the keys to a file
        keys_destiny_file = None
        
        if show_user_input:
            keys_destiny_file = input('Insert the name of keys file: \t')
        else:
            keys_destiny_file = getpass('Insert the name of keys file: \t')        
        
        write(keys_destiny_file, keys.get_keys(), '.rkeys')
        print('\nKeys file created: {}'.format(keys_destiny_file + '.rkeys'))
            
    else:
        # show the keys at the console
        keys.show_keys()

    
if __name__ == "__main__":
    main()
    print('\nDone')




