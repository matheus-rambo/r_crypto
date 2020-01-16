_READ_BINARY  = 'rb'
_WRITE_BINARY = 'wb'

from .classes import Encrypted
from json import dumps
from datetime import datetime


def write(filename:str, content:bytes):
    with open(file = filename, mode = _WRITE_BINARY ) as file:
        file.write(content)


def read(file_name:str, chunk_size:int = 2048):
    byte_array = bytearray()
    buffer     = None
    with open(file = file_name, mode = _READ_BINARY) as file:        
        while True:
            buffer = file.read(chunk_size)
            if buffer:
                for byte in buffer:
                    byte_array.append(byte)
            else:
                break
    return bytes(byte_array)

def generate_info(extension: str = None):
    info_tuple = None
    info_tuple = {
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'author': 'Ramboso Killer'
        }     
    return bytes(dumps(info_tuple).encode('ascii'))

def extract_info(byte_array:bytes):
    encrypted = Encrypted()
    print(byte_array)
    if byte_array[0:3] == b'\0\0\0':
        info_bytes_length = byte_array[3]
        # 3 null bytes and one byte to store the info length
        temp_size         = 4
        encrypted.message = byte_array[info_bytes_length + temp_size:]
        encrypted.info    = byte_array[4:info_bytes_length + temp_size]
    else:
        # compatible with older versions
        encrypted.message = byte_array 

    return encrypted

def persist_info(byte_array:bytes, extension:str = None):
    info        = generate_info(extension)
    info_length = len(info)

    # we write 3 null bytes, so we can make it compatible with older
    # versions when reading
    temp_bytes  = bytearray('\0\0\0'.encode('ascii'))
    temp_bytes.append(info_length)

    for byte in info:
        temp_bytes.append(byte)
    
    for byte in byte_array:
        temp_bytes.append(byte)
    
    return bytes(temp_bytes)


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


