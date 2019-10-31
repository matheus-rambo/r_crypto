from InvalidFileExtensionException import InvalidFileExtensionException

r_encrypt_extension = ".rencrypted"
r_decrypt_extension = ".rdecrypted"

def write_to_file(content:str, filename:str, isEncrypt:bool):
    if '.' in filename:
        index = filename.index('.')
        user_extension = filename[index:]
        filename = filename[:index]
        if isEncrypt == True:
            if user_extension != r_encrypt_extension:
                print("We are changing the extension of your file.\nTo use the standard rcrypt encrypted files: {}".format(r_encrypt_extension))
        else:
            if user_extension != r_decrypt_extension:
                print("We are changing the extension of your file.\nTo use the standard rcrypt decrypted files: {}".format(r_decrypt_extension))    
    filename = filename + r_encrypt_extension
    print("The content is on the file: {}".format(filename))
    file = open(filename, "ab+")
    file.write(content.decode("utf-8").encode("utf-8"))
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