import r_crypto as r_crypto
import r_file as r_file
import sys
from RCrypto import UserFile

sys_args_length = len(sys.argv)

def doCryptographyAction(filename:str, key:str):
    file = r_file.open_file(filename)
    content = r_file.read_file_lines(file)
    file.close()
    fernet = r_crypto.generate_custom_key(key)

    if (input("\nSave to a file: yes or no? ") in ("yes", "y")):
        content = r_file.set_info_to_a_file(content, filename)
        ciphed = r_crypto.encrypt(fernet, content)
        file_writter = input("Insert the name of the file: ")
        new_file = UserFile(file_writter)
        r_file.write_to_file(ciphed, new_file.file_name, new_file.extension, True)
    else:
        ciphed = r_crypto.encrypt(fernet, content)
        print(ciphed.decode('utf-8'))

if sys_args_length == 3:
    doCryptographyAction(sys.argv[1], sys.argv[2])
elif sys_args_length == 2:
    doCryptographyAction(sys.argv[1], input("Insert your key: "))
else:
    doCryptographyAction(input("Insert your file: "), input("Insert your key: "))


    

