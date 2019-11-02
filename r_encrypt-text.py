import r_crypto as r_crypto
from r_file import write_to_file
import sys
from RCrypto import UserFile

sys_args_length = len(sys.argv)

def doCryptographyAction(content:str, key:str):
    fernet = r_crypto.generate_custom_key(key)
    ciphed = r_crypto.encrypt(fernet, content)
    if (input("Save to a file: yes or no? ") in ("yes", "y")):
        file_writter = input("Insert the name of the file: ")
        new_file = UserFile(file_writter)        
        write_to_file(ciphed, new_file.file_name, new_file.extension, True)
    else:
        print(ciphed.decode('utf-8'))

if sys_args_length == 3:
    doCryptographyAction(sys.argv[1], sys.argv[2])
elif sys_args_length == 2:
    doCryptographyAction(sys.argv[1], input("Insert your key: "))
else:
    doCryptographyAction(input("Insert your text: "), input("Insert your key: "))


    

