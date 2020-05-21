_READ_BINARY  = 'rb'
_WRITE_BINARY = 'wb'

from datetime import datetime
from getpass  import getuser


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

def generate_info( message:str, filename: str = None):
    info = None
    if filename:
        info = '{};\0;{};\0;{};\0;{}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), getuser(), message, filename)
    else:
        info = '{};\0;{};\0;{}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), getuser(), message)
    return bytes(info.encode('utf-8'))


def persist_info(byte_array:bytes, message:str = 'User that encrypted did not let a message to you.', filename:str = None):
    info        = generate_info(message, filename)
    
    # we write 3 null bytes, so we can make it compatible with older
    # versions when reading
    temp_bytes  = bytearray(b'\0\0\0')
    
    for byte in info:
        temp_bytes.append(byte)
    
    # we will write 3 null bytes to specify the end of the info
    temp_bytes.append(0)
    temp_bytes.append(0)
    temp_bytes.append(0)

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

def get_file_from_absolute_path(path:str):
    if '/' in path:
        return path[path.rindex('/') + 1:] 
    elif '\\' in path:
        return path[path.rindex('\\') + 1:] 
    else:
        return path

def get_all_files_from_directory(directory:str, recursively:bool = False):
    import os
    files = []
    for item in os.listdir(directory):
        path = '{dir}/{file}'.format(dir = directory, file = item)
        if recursively and os.path.isdir(path):
            # merge lists
            files = files + get_all_files_from_directory(path, recursively) 
        else:
            files.append(path)
    return files


