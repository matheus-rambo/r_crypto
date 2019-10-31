import r_crypto as r_crypto
import r_file as r_file
import sys

sys_args_length = len(sys.argv)

def doCryptographyAction(filename:str, key:str):
    file = r_file.open_file(filename)
    content = r_file.read_file_lines(file)
    fernet = r_crypto.generate_custom_key(key)
    ciphed = r_crypto.encrypt(fernet, content)
    print("Content encrypted!\n")
    if (input("Save to a file: yes or no? ") in ("yes", "y")):
        file_writter = input("Insert the name of the file: ")
        r_file.write_to_file(ciphed, file_writter, True)
    else:
        print(ciphed.decode('utf-8'))

if sys_args_length == 3:
    doCryptographyAction(sys.argv[1], sys.argv[2])
elif sys_args_length == 2:
    doCryptographyAction(sys.argv[1], input("Insert your key: "))
else:
    doCryptographyAction(input("Insert your file: "), input("Insert your key: "))


    

