import source.r_crypto as r_crypto
import source.r_file as r_file
import sys
from source.RCrypto import UserFile
from getpass import getpass


sys_args_length = len(sys.argv)

def doCryptographyAction(filename:str, key:str):
    file = r_file.open_file(filename)
    content = r_file.read_file_lines(file)
    file.close()
    fernet = r_crypto.generate_custom_key(key)

    if input("\nSave to a file? [yes, no]: ") in ("yes", "y", "Yes", "YES"):
        content = r_file.set_info_to_a_file(content, filename)
        ciphed = r_crypto.encrypt(fernet, content)
        file_writter = input("Insert the name of the file: ")
        new_file = UserFile(file_writter)
        r_file.write_to_file(ciphed, new_file.file_name, new_file.extension, True)
    else:
        ciphed = r_crypto.encrypt(fernet, content)
        print(ciphed.decode('utf-8'))

    if input("\n\nDo you want to remove the original file: {}? [yes, no]: ".format(filename)) in ("yes", "y", "Yes", "YES"):
            from os import remove
            remove(filename)


if sys_args_length == 3:
    doCryptographyAction(sys.argv[1], sys.argv[2])
elif sys_args_length == 2:
    doCryptographyAction(sys.argv[1], getpass("Insert your key: "))
else:
    doCryptographyAction(input("Insert your file: "), getpass("Insert your key: "))


    

