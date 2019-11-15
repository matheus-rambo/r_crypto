import sys
from source.r_file import get_file_extension, is_an_image

args_length = len(sys.argv)

def stenography(hidden_file_path:str):
    extension = get_file_extension(hidden_file_path)
    if is_an_image(extension):
        secret_message = None
        if extension in (".jpeg", ".jpg"):
            from stegano import exifHeader
            secret_message = exifHeader.reveal(hidden_file_path)
        else:
            from stegano import lsb
            secret_message = lsb.reveal(hidden_file_path)        

        print("The secret message is: {}".format(secret_message))
        print("\nDone!")
    else:
        print("The extension: {} is not in an image format!".format(extension))   

if args_length >= 2:
    stenography(sys.argv[1])
elif args_length == 1:
    stenography(input("Insert the path of the hidden image: "))