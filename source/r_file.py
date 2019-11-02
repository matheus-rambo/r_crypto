from .RCrypto import InvalidFileExtensionException, Info
from getpass import getuser
from datetime import datetime

current_version = "v1.3"
r_encrypt_extension = ".rencrypted"

def get_file_extension(file:str): 
    if "." in file:
        index = file.rindex(".")
        return file[index:]
    else:
        return ""

def set_info_to_a_file(content:str, filename:str):
    current_user = getuser()
    file_extension = get_file_extension(filename)
    current_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    additional_info = "#RCRYPTO Information#;{};{};{};{}".format(current_user, current_time, file_extension, current_version)
    return content + additional_info

def get_file_information(content:str):
    info = Info()
    if "#RCRYPTO Information#" in content:
        info_index = content.rindex("#RCRYPTO Information#")
        info.content = content[:info_index]
        info.set_information(content[info_index:])
    else:
        info.content = content
    return info

def write_to_file(content:str, filename:str, extension: str, isEncrypt:bool):
    if '.' in extension:
        if isEncrypt:
            filename = filename + r_encrypt_extension
            if extension != r_encrypt_extension:
                print("We are changing the extension that you defined to support our encrypted extensions. From: {} to: {}".format(extension, r_encrypt_extension))
        else:
            filename = filename + extension
    else:
        if isEncrypt:
            filename = filename + r_encrypt_extension
        else:
            # Thats a case when user encrypt a text, and then he decrypts it, and choose to save.
            # so, we will define the extension as .txt
            filename = filename + ".txt"
    print("The content is on the file: {}".format(filename))
    file = open(filename, "ab+")
    if type(content) is str:
        file.write(content.encode("utf-8"))
    else:
        file.write(content)
    file.close()

def open_file(filename:str):
    file = open(filename, "r", encoding='utf-8')
    return file

def open_rcrypted_file(filename:str):
    if r_encrypt_extension not in filename:
        string = "Your are using an invalid rcrypt file!\nIf you want to decrypt a file with r_crypt, you must pass an <file>{}".format(r_encrypt_extension)
        raise InvalidFileExtensionException(string)
    else:
        return open_file(filename)

def read_file_lines(file):
    return file.read()
   




