import argparse
from getpass import getpass
from source.classes import Cryptor, Keys
from source.app_util import write, read, read_ask_answear, read_data_from_console


parser = argparse.ArgumentParser(description='Encrypt/Decrypt text and text files with this script. With this tool, you can encrypt/decrypt files, and texts, then save them, load file of keys and creates keys file.')

parser._action_groups.pop()

required = parser.add_argument_group('required arguments')
optional = parser.add_argument_group('optional arguments')

# required arguments
required.add_argument('-is-file', type=int, choices=[1,0], help='If you want to work over a file, otherwise a text will be used', required=True, dest='is_file')
required.add_argument('-is-encryption', type=int, choices=[1,0], help='If you want to work with encryption, otherwise we will decrypt', required=True, dest='is_encryption')


# optional arguments
optional.add_argument('--save-content', type=int, choices=[1, 0], default=0,  help='If you want to save the encrypted/decrypted content to a file, otherwise it will be prompted at console.', dest='save_content')
optional.add_argument('--show', type=int, choices=[1, 0], default=0, help='Show the characters that you typed.', dest='show_user_input')
optional.add_argument('--secret-key-computed', type=int, choices=[1,0], default=0, help='If you have an secret key that was generated with your key, you can use it here.', dest='is_secret_key_computed' )
optional.add_argument('--save-keys', type=int, choices=[1,0], default=0, help='If you want to save the keys at a file. Otherwise, the keys will be prompted.', dest='save_keys')
optional.add_argument('--chunk-size', type=int, default=2048, help='Size of bytes to read at time.', dest='chunk_size')
optional.add_argument('--read-keys-file', type=int, choices=[1, 0], default=0, help='If you have a keys file, you can read it.', dest='read_keys_file')
optional.add_argument('--charset', type=str, choices=['utf-8', 'utf-16', 'ascii'], default='utf-8', help='Charset that you want to use.')
optional.add_argument('--send-mail', type=int, choices=[1,0], default=0, help='If you want to send the content over e-mail', dest='send_mail')


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

# Size of bytes to read at time
chunk_size = args.chunk_size

# if the user wants to read the keys from a file
read_keys_file = args.read_keys_file

# charset
charset = args.charset

# if the user want to send an e-mail
send_mail = args.send_mail

def keys_stage():
    print('\n\tInit keys stage . . . ')
    key = None
    secret_key = None
    if read_keys_file:
        from json import loads
        keys_file    = read_data_from_console('Insert the name of yours keys file:\t', show_user_input)
        byte_array   = read(keys_file, chunk_size)
        keys_content = byte_array.decode(charset)
        key          = loads(keys_content)['key']
        secret_key   = loads(keys_content)['secret_key']
        print('\nKeys were loaded') 
    else:
        key = read_data_from_console('Insert your key:\t', show_user_input)
        if is_secret_key_computed or not is_encryption:
            secret_key = read_data_from_console('Insert your secret key:\t', show_user_input)
    
    print('\n\tKeys stage was finished!')
    return {
        'key': key,
        'secret_key': secret_key
    }

def read_user_content_stage():
    print('\n\tInit read user content stage . . .\n')
    # we will store the bytes
    bytes_array = []
    if is_file:
        print('For two or more files, type: file1 file2 file3 . . .')
        files_string = read_data_from_console('Insert the path of the file(s):\t', show_user_input)
        files = files_string.split(' ')
        for file_name in files:
            print('Reading content of the file: {}'.format(file_name))
            bytes_array.append(read(file_name, chunk_size))
    else:
        if is_encryption:
            message = read_data_from_console('Insert the message:\t', show_user_input)
            bytes_array.append(bytes(message.encode(charset)))
        else:
            message = read_data_from_console('Insert the encrypted message:\t', show_user_input)
            bytes_array.append(bytes(message.encode(charset)))

    print('\n\tRead user content stage was finished!')
    return bytes_array


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
        file_name = read_data_from_console('Insert the name of {} file:\t'.format(message), show_user_input)
        message = None
        if is_encryption and read_ask_answear('Do you want to store a message inside the file? [Yes, No]: ', True):
            message = read_data_from_console('Your message: ')
            write(file_name, content, extension, True, bytes(message.encode(charset)))
        else:
            write(file_name, content, extension, is_encryption, None)

    print('File created: {}'.format(file_name + extension))

    print('\n\tSave content stage was finished!')

def print_content_stage(contents:list):
    print('\n\tInit print content stage . . .\n')
    message = 'Your encrypted content:\t{}\n' if is_encryption else 'Your decrypted content:\t{}\n'
    for content in contents:
        print(message.format(content.decode(charset)))
    print('\tPrint content stage finished!')    


def save_keys_stage(keys:Keys):
    print('\n\tInit save keys stage . . .\n')
    keys_file = read_data_from_console('Insert the name of keys file:\t', show_user_input)
    write(keys_file, bytes(keys.get_keys().encode(charset)), '.rkeys')
    print('File created: {}'.format(keys_file + '.rkeys'))
    print('\n\tSave keys stage was finished!')

def print_keys_stage(keys: Keys):
    print('\n\tInit print keys stage . . .\n')
    keys.show_keys()
    print('\n\tPrint keys stage was finished!')


def send_mail_stage(content: [], keys:str):
    from source.mail import Mail
    print('\n\tInit send e-mail stage . . .\n')
    
    mail = Mail()
    formatted = 'encrypted' if is_encryption else 'decrypted'
    contacts = None

    if read_ask_answear('\nDo you want to send an e-mail with the {} content? [Yes, No]: '.format(formatted), show_user_input):
        contacts = read_data_from_console('\nType the contacts to send e-mail. Use a comma to separete receivers.\n', show_user_input)
        string_content = '\n\n{aux} ATTENTION: BELOW THIS LINE, IT\'S ANOTHER {type} CONTENT {aux}\n\n'.format(aux = 30 * '-', type = 'ENCRYPTED' if is_encryption else 'DECRYPTED').join(content.decode('utf-8'))
        subject =  read_data_from_console('\nSubject: ', show_user_input)
        mail.send_email(contacts, string_content, '{}.txt'.format(formatted), subject)

    if is_encryption and read_ask_answear('\nDo you want to send an e-mail with the keys to decrypt? [Yes, No]: ', True):
        if not (contacts is not None and read_ask_answear('\nDo you want to use the same contacts? [Yes, No]: ', True)):
            contacts = read_data_from_console('Type the contacts to send e-mail. Use a comma to separete receivers.\n', show_user_input)
        subject =  read_data_from_console('\nSubject: ', show_user_input)
        mail.send_email(contacts, keys, 'decryption_keys.rkeys', subject)

    print('\n\tSend e-mail stage was finished!')


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


    if send_mail:
        send_mail_stage(content, cryptor.keys.get_keys())

    
if __name__ == "__main__":
    main()
    print('\nDone.\tHave a nice day.')
