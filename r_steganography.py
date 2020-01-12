import argparse
from source.app_util import read, read_data_from_console, get_file_extension, read_ask_answear

parser = argparse.ArgumentParser(description='Hide/Reveal messages inside an image file')

parser._action_groups.pop()

required = parser.add_argument_group('required arguments')
optional = parser.add_argument_group('optional arguments')

required.add_argument('-is-hide', type=int, choices=[1,0], help='If you want hide and message, otherwise we will reveal a message from an image file', required=True, dest='is_hide')

optional.add_argument('--buffer-size', type=int, default=2048, help='Buffer size when reading the message from a file', dest='buffer_size')
optional.add_argument('--show', type=int, choices=[1,0], default=0, help='If you want to see what you are typing.', dest='show')
optional.add_argument('--charset', type=str, choices=['utf-8', 'utf-16'], default='utf-8', dest='charset')
optional.add_argument('--send-mail', type=int, choices=[1,0], default=0, help='If you want to send the content over e-mail', dest='send_mail')

args = parser.parse_args()

is_hide     = args.is_hide
buffer_size = args.buffer_size
show        = args.show
charset     = args.charset
send_mail   = args.send_mail

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
    if read_ask_answear('Do you want to read the message from a file? [Yes, No]\t', True):
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

    else:
        raise Exception('Extension {} not supported!'.format(extension))

    print('\n\tHide message stage finished!')
    return file_with_message


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
    else:
        raise Exception('Extension {} not supported!'.format(extension))
    print('Secret message is:\t{}'.format(secret_message.decode(charset)))
    print('\n\tReveal message stage finished!')

def send_mail_stage(image_path : str):
    from source.mail import Mail
    print('\n\tInit Send mail stage . . .')
    
    images   = []
    contacts = read_data_from_console('\nType the contacts to send e-mail. Use a comma to separete receivers.\n', show)
    subject  = read_data_from_console('Subject: ', show)
    mail     = Mail()

    if read_ask_answear('Do you want to attach more images to difficult the discover of steganography? [Yes, No]: ', True):
        print('\n\tKeyboard Interrupt to stop... (Control + C)')
        while True:
            try:
                images.append(read_data_from_console('Image path: ', show))
            except KeyboardInterrupt:
                print('\nStopping . . .\n')
                break

    images.append(image_path)
    mail.send_email_with_images(contacts, images, subject)
    
    print('\n\tSend mail stage finished!')


def main():
    
    if is_hide:
        image_file_name = open_image_file_stage()
        message         = read_secret_message_stage()
        hidden_file     = hide_message_stage(message, image_file_name)
        if send_mail:
            send_mail_stage(image_path = hidden_file)
    else:
        image_file_name = open_image_file_stage()
        reveal_message_stage(image_file_name)        


if __name__ == "__main__":
    main()
    pass