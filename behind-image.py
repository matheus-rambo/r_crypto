import sys
from source.r_file import get_file_extension, is_an_image


args_length = len(sys.argv)

def open_file_if_exists(file_path:str):
    try:
        return open(file_path, "rt")
    except Exception:
        return None

def read_file_content(file_path:str):
    file = open_file_if_exists(file_path)
    if file is not None:
        return file.read()
    return file_path

def stenography(original_file_path:str, secret_message:str):
    extension = get_file_extension(original_file_path)
    if is_an_image(extension):
        if extension in (".jpeg", ".jpg"):
            from stegano import exifHeader
            exifHeader.hide(original_file_path, input("Choose a name for the hidden file: ") + extension , secret_message)
        else:
            from stegano import lsb
            secret = lsb.hide(original_file_path, secret_message)
            secret.save(input("Choose a name for the hidden file: ") + extension)
        
        print("\nDone!")

    else:
        print("The extension: {} is not in an image format!".format(extension))    

if args_length == 2:
    content = read_file_content(input("Insert the secret message to hide: "))
    stenography(sys.argv[1], content)
elif args_length >= 3:
    content = read_file_content(sys.argv[2])
    stenography(sys.argv[1], content)
else:
    stenography(input("Insert the name of the file to copy and hide the information: "), read_file_content(input("Insert the secret message to hide: ")))

