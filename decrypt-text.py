from source.r_crypto import generate_key, decrypt
import source.r_file as r_file
import sys
from source.RCrypto import UserFile

sys_args_length = len(sys.argv)

def doCryptographyAction(content:str, key:str, secret_key: str):
    fernet = generate_key(key, secret_key)
    ciphed = decrypt(fernet, content)
    print("Content decrypted!\n")
    if input("Save to a file? yes or no ") in ("yes", "y"):
         file_writter = input("Insert the name of the file: ")
         new_file = UserFile(file_writter)
         r_file.write_to_file(ciphed, new_file.file_name, new_file.extension, False)
    else:
        print(ciphed.decode('utf-8'))    

if sys_args_length == 4:
    content = sys.argv[1]
    key = sys.argv[2]
    secret_key = sys.argv[3]
    doCryptographyAction(content, key, secret_key)
elif sys_args_length == 3:
    content = sys.argv[1]
    key = sys.argv[2]
    doCryptographyAction(content, key, input("Insert your secret key: "))
elif sys_args_length == 2:
    content = sys.argv[1]
    doCryptographyAction(content, input("Insert your key: "), input("Insert your secret key: "))
else:
    doCryptographyAction(input("Insert your text: "), input("Insert your key: "), input("Insert your secret key: "))
