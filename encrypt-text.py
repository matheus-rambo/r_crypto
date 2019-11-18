import source.r_crypto as r_crypto
from source.r_file import write_to_file
import sys
from source.RCrypto import UserFile
from getpass import getpass


sys_args_length = len(sys.argv)

def doCryptographyAction(content:str, key:str):
    fernet = r_crypto.generate_custom_key(key)
    ciphed = r_crypto.encrypt(fernet, content)
    if input("\nSave to a file? [yes, no]: ") in ("yes", "y", "Yes", "YES"):
        file_writter = input("Insert the name of the file: ")
        new_file = UserFile(file_writter)        
        write_to_file(ciphed, new_file.file_name, new_file.extension, True)
    else:
        print(ciphed.decode('utf-8'))

if sys_args_length >= 2:
    doCryptographyAction(sys.argv[1], getpass("Insert your key: "))
else:
    doCryptographyAction(input("Insert your text: "), getpass("Insert your key: "))


    

