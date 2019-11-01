from r_crypto import generate_key, decrypt
import r_file as r_file
import sys

sys_args_length = len(sys.argv)

def doCryptographyAction(file_name:str, key:str, secret_key: str):
    file = r_file.open_rcrypted_file(file_name)
    content = r_file.read_file_lines(file)
    file.close()
    fernet = generate_key(key, secret_key)
    ciphed = decrypt(fernet, content)
    print("Content decrypted!\n")
    if input("Save to a file? yes or no ") in ("yes", "y"):
         file_writter = input("Insert the name of the file: ")
         r_file.write_to_file(ciphed, file_writter, False)
    else:
        print(ciphed.decode('utf-8'))    


if sys_args_length == 4:
    file_name = sys.argv[1]
    key = sys.argv[2]
    secret_key = sys.argv[3]
    doCryptographyAction(file_name, key, secret_key)
elif sys_args_length == 3:
    file_name = sys.argv[1]
    key = sys.argv[2]
    doCryptographyAction(file_name, key, input("Insert your secret key: "))
elif sys_args_length == 2:
    file_name = sys.argv[1]
    doCryptographyAction(file_name, input("Insert your key: "), input("Insert your secret key: "))
else:
    doCryptographyAction(input("Insert your filename: "), input("Insert your key: "), input("Insert your secret key: "))
