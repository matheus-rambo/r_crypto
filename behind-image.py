import sys
from source.r_file import get_file_extension, is_an_image


args_length = len(sys.argv)

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
    stenography(sys.argv[1], input("Insert the secret message to hide: "))
elif args_length >= 3:
    stenography(sys.argv[1], sys.argv[2])
else:
    stenography(input("Insert the name of the file to copy and hide the information: "), input("Insert the secret message to hide: "))

