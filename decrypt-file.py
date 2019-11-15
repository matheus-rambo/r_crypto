from source.r_crypto import generate_key, decrypt
import source.r_file as r_file
import sys
from source.RCrypto import Info
from getpass import getpass

sys_args_length = len(sys.argv)

def doCryptographyAction(files: [], key:str, secret_key: str):
    fernet = generate_key(key, secret_key)
    for file_name in files:
        print("\nInit decryption for: {}".format(file_name))
        file = r_file.open_rcrypted_file(file_name)
        content = r_file.read_file_lines(file)
        file.close()
        ciphed = decrypt(fernet, content)
        info = r_file.get_file_information(ciphed.decode('utf-8'))
        
        if input("\nSave to a file? [Yes, No]: ") in ("yes", "y", "Yes", "YES"):
            r_file.write_to_file(info.content, file_name, info.get_original_file_extension(), False)
            info.print_info()
        else:
            info.print_all()    
        if input("\n\nDo you want to remove the original file: {}? [Yes, No]: ".format(file_name)) in ("yes", "y", "Yes", "YES"):
            from os import remove
            remove(file_name)
    print("\nDone!")

if sys_args_length == 1:
    files = []
    files.append(input("Insert your file: "))
    doCryptographyAction(files, getpass("Insert your key: "), getpass("Insert your secret key: "))
else:
    files = sys.argv[1:]
    doCryptographyAction(files, getpass("Insert your key: "), getpass("Insert your secret key: "))
