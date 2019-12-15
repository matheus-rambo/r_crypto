import argparse
from source.app_util import read_file_content, read_data_from_console, get_file_extension


parser = argparse.ArgumentParser(description='Hide/Reveal messages inside an image file')

parser._action_groups.pop()

required = parser.add_argument_group('required arguments')
optional = parser.add_argument_group('optional arguments')

required.add_argument('-is-hide', type=int, choices=[1,0], help='If you want hide and message, otherwise we will reveal a message from an image file', required=True, dest='is_hide')

optional.add_argument('--buffer-size', type=int, default=2048, help='Buffer size when reading the message from a file', dest='buffer_size')
optional.add_argument('--show', type=int, choices=[1,0], default=0, help='If you want to see what you are typing.', dest='show')
optional.add_argument('--charset', type=str, choices=['utf-8'], default='utf-8', dest='charset')

args = parser.parse_args()

is_hide = args.is_hide
buffer_size = args.buffer_size
show = args.show
charset= args.charset

def open_image_file_stage():
    print('\n\tInit get image file stage . . .')
    image_file = None
    if is_hide:
        image_file = read_data_from_console('Insert the path of the image file that you want to hide an message:\t', show)
    else:
        image_file = read_data_from_console('Insert the path of the image file that you want reveal:\t', show)
        
    
    print('\n\tGet image file finished!')
    return image_file

def read_secret_message_stage():
    print('\n\tInit read secret message stage . . .')
    message = None
    if input('Do you want to read the message from a file? [Yes, No]\t').lower()[0] == 'y':
        file_name = read_data_from_console('Insert the file name:\t', show)
        message = read_file_content(file_name, buffer_size)
    else:
        message = read_data_from_console('Insert your message:\t', show)
    print('\n\tRead secret message stage finished!')
    return message


def hide_message_stage(message:str, image_file_name:str):
    print('\n\tInit hide message stage . . .')
    extension = get_file_extension(image_file_name)
    file_with_message = read_data_from_console('Choose a name for the image with hidden message:\t', show)
    
    # we will remove the extension that the user choosed
    if '.' in file_with_message:
        index = file_with_message.rindex('.')
        file_with_message = file_with_message[0:index]

    file_with_message = file_with_message + extension
    if extension in ('.jpeg', '.jpg'):
        from stegano import exifHeader
        exifHeader.hide(image_file_name, file_with_message, message)

    elif extension == '.png':
        from stegano import lsb
        secret = lsb.hide(image_file_name, message)
        secret.save(file_with_message)

    print('\n\tHide message stage finished!')


def reveal_message_stage(image_file_name:str):
    print('\n\tInit reveal message stage . . .')
    extension = get_file_extension(image_file_name)
    secret_message = None
    if extension in ('.jpeg', '.jpg'):
        from stegano import exifHeader
        secret_message = exifHeader.reveal(image_file_name)
    elif extension == '.png':
        from stegano import lsb
        secret_message = lsb.reveal(image_file_name)
    print('Secret message is:\t{}'.format(secret_message.decode(charset)))
    print('\n\tReveal message stage finished!')


def main():
    
    if is_hide:
        image_file_name = open_image_file_stage()
        message = read_secret_message_stage()
        hide_message_stage(message, image_file_name)
    else:
        image_file_name = open_image_file_stage()
        reveal_message_stage(image_file_name)        


if __name__ == "__main__":
    main()
    pass