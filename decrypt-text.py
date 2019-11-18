from source.r_crypto import generate_key, decrypt
import source.r_file as r_file
import sys
from source.RCrypto import UserFile
from getpass import getpass

sys_args_length = len(sys.argv)

def doCryptographyAction(content:str, key:str, secret_key: str):
    fernet = generate_key(key, secret_key)
    ciphed = decrypt(fernet, content)
    print("Content decrypted!\n")
    if input("\nSave to a file? [yes, no]: ") in ("yes", "y", "Yes", "YES"):
         file_writter = input("Insert the name of the file: ")
         new_file = UserFile(file_writter)
         r_file.write_to_file(ciphed, new_file.file_name, new_file.extension, False)
    else:
        print("\nYour content")
        print(ciphed.decode('utf-8'))    

if sys_args_length >= 2:
    content = sys.argv[1]
    doCryptographyAction(content, getpass("Insert your key: "), getpass("Insert your secret key: "))
else:
    doCryptographyAction(input("Insert your text: "), getpass("Insert your key: "), getpass("Insert your secret key: "))
