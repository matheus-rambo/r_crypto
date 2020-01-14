_READ_BINARY  = 'rb'
_WRITE_BINARY = 'wb'


def write(filename:str, content:bytes, extension:str, is_encryption:bool = False, message:bytes = None):
    if '.' in filename:
        index = filename.rindex('.')
        filename = filename[0:index]
    filename = filename + extension

    with open(file = filename, mode = _WRITE_BINARY ) as file:

        if is_encryption:

            if message is not None:
                # we will write yes, so wen we decrypt we can restore the message
                file.write('YES'.encode('ascii'))    
                
                # we will store how many bytes we need to store the message
                message_size = len(message)

                # convert the size of the message to bytes
                message_bytes = message_size.to_bytes((message_size.bit_length() + 7) // 8, 'big')   

                file.write(message_bytes)
                file.write(message)


            else:
                # we will write NO with a Null byte so the length is the same as the yes word
                # so when we decrypt the file, we will no that thre is not a message to retrieve
                file.write('NO\0'.encode('ascii'))


        file.write(content)


def read(file_name:str, chunk_size:int = 2048):
    byte_array = bytearray()
    buffer     = None
    with open(file = file_name, mode = _READ_BINARY) as file:
        try:
            has_message = file.read(3).decode()
            if has_message == 'YES':
                size = int.from_bytes(bytes = file.read(1), byteorder='big')
                message = file.read(size)
                print(message)
            elif has_message != 'NO\0':
                file.seek(0)
        except UnicodeDecodeError:
            print('Error')
            file.seek(0)
        while True:
            buffer = file.read(chunk_size)
            if buffer:
                for byte in buffer:
                    byte_array.append(byte)
            else:
                break
    return bytes(byte_array)

    
def read_data_from_console(message: str, show_input: bool = True):
    if show_input:
        return input(message)
    else:
        from getpass import getpass
        return getpass(message)

def get_file_extension(file_name: str):
    last_index = file_name.rindex('.')
    return file_name[last_index:] 

def read_ask_answear(message:str, show_input: bool = False):
    answear = read_data_from_console(message, show_input) 
    return False if ( answear is None or answear.strip() == '' ) else answear.lower()[0] == 'y'


