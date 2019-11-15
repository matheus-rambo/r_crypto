import source.r_crypto as r_crypto
import source.r_file as r_file
import sys
from source.RCrypto import UserFile
from getpass import getpass


sys_args_length = len(sys.argv)

def doCryptographyAction(files:[], key:str):
    fernet = r_crypto.generate_custom_key(key)
    for file_name in files:
        file = r_file.open_file(file_name)
        content = r_file.read_file_lines(file)
        file.close()
        print("\nInit encryption for {}".format(file_name))
        if input("\nSave to a file? [Yes, No]: ") in ("yes", "y", "Yes", "YES"):
            content = r_file.set_info_to_a_file(content, file_name)
            ciphed = r_crypto.encrypt(fernet, content)
            new_file = UserFile(file_name)
            r_file.write_to_file(ciphed, new_file.file_name, new_file.extension, True)
        else:
            ciphed = r_crypto.encrypt(fernet, content)
            print(ciphed.decode('utf-8'))
        
        if input("\n\nDo you want to remove the original file: {}? [Yes, No]: ".format(file_name)) in ("yes", "y", "Yes", "YES"):
            from os import remove
            remove(file_name)
    print("\nDone!")

if sys_args_length == 1:
    files = []
    files.append(input("Insert your file: "))
    doCryptographyAction(files, getpass("Insert your key: "))
else:
    files = sys.argv[1:]
    doCryptographyAction(files, getpass("Insert your key: "))

