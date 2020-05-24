import argparse

from source.main import Main

parser = argparse.ArgumentParser(description='Encrypt/Decrypt text/files and files from directory.')

parser._action_groups.pop()

required = parser.add_argument_group('required arguments')
optional = parser.add_argument_group('optional arguments')

# required arguments
required.add_argument('-use', type=str, choices=['text', 'file', 'directory'], help='What you want to work with ?', required=True, dest='use')
required.add_argument('-encryption', type=int, choices=[1,0], help='If you want to encrypt something.', required=True, dest='encryption')


# optional arguments
optional.add_argument('--save-content', type=int, choices=[1, 0], default=0,  help='If you want to save the encrypted/decrypt content, otherwise, the content will be show in the console.', dest='save_content')
optional.add_argument('--show-input', type=int, choices=[1, 0], default=0, help='If you want to see what you are typing.', dest='show_input')
optional.add_argument('--secret-key-computed', type=int, choices=[1,0], default=0, help='If you already have a secret key and want to use it.', dest='secret_key_computed' )
optional.add_argument('--save-keys', type=int, choices=[1,0], default=0, help='If you want to save the keys at a file. Otherwise, the keys will be prompted.', dest='save_keys')
optional.add_argument('--chunk-size', type=int, default=2048, help='Size of bytes to read at time.', dest='chunk_size')
optional.add_argument('--read-keys-file', type=int, choices=[1, 0], default=0, help='If you have a keys file, you can read the keys from it.', dest='read_keys_file')
optional.add_argument('--charset', type=str, choices=['utf-8', 'utf-16', 'ascii'], default='utf-8', help='Charset that you want to use.')


# we get the command line arguments
args = parser.parse_args() 

# What user wants to use, a file, text or directory
use = args.use

# if user wants to encrypt
encryption = args.encryption

# if user wants to save the encrypted content
save_content = args.save_content

# if user want to see his inputs
show_input = args.show_input

# if the user already has an computed secret key, if yes, we will ask him to input and then create
# the Fernet with his keys
secret_key_computed = args.secret_key_computed

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


def main():
    
    main = Main(use, encryption, save_content, show_input, secret_key_computed, save_keys, chunk_size, read_keys_file, charset)
    main.init()

if __name__ == "__main__":
    main()
    print('\nDone.\tHave a nice day.')
