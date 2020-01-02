import argparse
from getpass import getpass
from source.classes import Cryptor, Keys
from source.app_util import write, read_file_content


parser = argparse.ArgumentParser(description='Encrypt/Decrypt text and text files with this script. With this tool, you can encrypt/decrypt files, and texts, then save them, load file of keys and creates keys file.')

parser._action_groups.pop()

required = parser.add_argument_group('required arguments')
optional = parser.add_argument_group('optional arguments')

# required arguments
required.add_argument('-is-file', type=int, choices=[1,0], help='If you want to work over a file, otherwise a text will be used', required=True, dest='is_file')
required.add_argument('-is-encryption', type=int, choices=[1,0], help='If you want to work with encryption, otherwise we will decrypt', required=True, dest='is_encryption')


# optional arguments
optional.add_argument('--save-content', type=int, choices=[1, 0], default=0,  help='If you want to save the encrypted content to a file, otherwise it will be prompted at console.', dest='save_content')
optional.add_argument('--show', type=int, choices=[1, 0], default=0, help='Show the characters that you typed.', dest='show_user_input')
optional.add_argument('--secret-key-computed', type=int, choices=[1,0], default=0, help='If you have an secret key that was generated with your key, you can use it here.', dest='is_secret_key_computed' )
optional.add_argument('--save-keys', type=int, choices=[1,0], default=0, help='If you want to save the keys at a file. Otherwise, the keys will be prompted.', dest='save_keys')
optional.add_argument('--buffer-size', type=int, default=2048, help='Size of the buffer when reading data from a file.', dest='buffer_size')
optional.add_argument('--read-keys-file', type=int, choices=[1, 0], default=0, help='If you have a keys file, you can read it.', dest='read_keys_file')
optional.add_argument('--charset', type=str, choices=['utf-8', 'utf-16'], default='utf-8', help='Charset that you want to use.')


# we get the command line arguments
args = parser.parse_args() 


# if the users wants to encrypt a file
is_file = args.is_file

# if user wants to encrypt
is_encryption = args.is_encryption


# if user wants to save the encrypted content
save_content = args.save_content

# if user want to see his inputs
show_user_input = args.show_user_input

# if the user already has an computed secret key, if yes, we will ask him to input and then create
# the Fernet with his keys
is_secret_key_computed = args.is_secret_key_computed

# if the user want to save the keys at a file
save_keys = args.save_keys

# Size of buffer for reading characters of a text file
buffer_size = args.buffer_size

# if the user wants to read the keys from a file
read_keys_file = args.read_keys_file

# charset
charset = args.charset

def read_data_from_console(message: str):
    if show_user_input:
        return input(message)
    else:
        return getpass(message) 

def keys_stage():
    print('\n\tInit keys stage . . . ')
    key = None
    secret_key = None
    if read_keys_file:
        keys_file = read_data_from_console('Insert the name of yours keys file:\t')
        keys_content = read_file_content(keys_file, buffer_size, charset)
        from json import loads
        key = loads(keys_content)['key']
        secret_key = loads(keys_content)['secret_key']
        print('\nKeys were loaded') 
    else:
        key = read_data_from_console('Insert your key:\t')
        if is_secret_key_computed or not is_encryption:
            secret_key = read_data_from_console('Insert your secret key:\t')
    
    print('\n\tKeys stage was finished!')
    return {
        'key': key,
        'secret_key': secret_key
    }

def read_user_content_stage():
    print('\n\tInit read user content stage . . .\n')
    content_to_work = []
    if is_file:
        print('For two or more files, type: file1 file2 file3 . . .')
        files_string = read_data_from_console('Insert the path of the file(s):\t')
        files = files_string.split(' ')
        for file_name in files:
            print('Reading content of the file: {}'.format(file_name))
            content_to_work.append(read_file_content(file_name, buffer_size, charset))

    else:
        if is_encryption:
            content_to_work.append(read_data_from_console('Insert the message:\t'))
        else:
            content_to_work.append(read_data_from_console('Insert the encrypted message:\t'))

    print('\n\tRead user content stage was finished!')
    return content_to_work


def encrypt_stage(content: list, cryptor: Cryptor):
    encrypted_content = []
    print('\n\tInit encryption stage . . .\n')
    for index in range(0, len(content)):
        print('Encrypting content: {}'.format(index + 1))
        encrypted_content.append(cryptor.encrypt(content[index]))

    print('\n\tEncryption stage was finished!')
    return encrypted_content

def decrypt_stage(content: list, cryptor: Cryptor):
    decrypted_content = []
    print('\n\tInit decryption stage . . .\n')
    for index in range(0, len(content)):
        print('Decrypting content: {}'.format(index + 1))
        decrypted_content.append(cryptor.decrypt(content[index]))

    print('\n\tDecryption stage was finished!')
    return decrypted_content

def save_content_stage(contents: list):
    extension = '.rencrypted' if is_encryption else '.rdecrypted'
    message = 'encrypted' if is_encryption else 'decrypted'
    print('\n\tInit save content stage . . .\n')

    for content in contents:
        file_name = read_data_from_console('Insert the name of {} file:\t'.format(message))
        write(file_name, content, extension)
        print('File created: {}'.format(file_name + extension))

    print('\n\tSave content stage was finished!')

def print_content_stage(contents:list):
    print('\n\tInit print content stage . . .\n')
    message = 'Your encrypted content:\t{}\n' if is_encryption else 'Your decrypted content:\t{}\n'
    for content in contents:
        print(message.format(content))
    print('\tPrint content stage finished!')    


def save_keys_stage(keys:Keys):
    print('\n\tInit save keys stage . . .\n')
    keys_file = read_data_from_console('Insert the name of keys file:\t')
    write(keys_file, keys.get_keys(), '.rkeys')
    print('File created: {}'.format(keys_file + '.rkeys'))
    print('\nSave keys stage was finished!')

def print_keys_stage(keys: Keys):
    print('\n\tInit print keys stage . . .\n')
    keys.show_keys()
    print('\nPrint keys stage was finished!')




def main():      


    keys = keys_stage()
    content = read_user_content_stage()

    # cryptor object    
    cryptor = Cryptor(keys['key'], keys['secret_key'], charset)    
    
    if is_encryption:
        content = encrypt_stage(content, cryptor)
    else:
        content = decrypt_stage(content, cryptor)


    if save_content:
        save_content_stage(content)
    else:
        print_content_stage(content)

    if save_keys:
        save_keys_stage(cryptor.keys)
    else:
        print_keys_stage(cryptor.keys)

    
if __name__ == "__main__":
    main()
    print('\nDone')




