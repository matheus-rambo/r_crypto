_READ_BINARY  = 'rb'
_WRITE_BINARY = 'wb'


def write(file_name:str, content:bytes, extension:str):
    if '.' in file_name:
        index = file_name.rindex('.')
        file_name = file_name[0:index]
    file_name = file_name + extension
    with open(file = file_name, mode = _WRITE_BINARY ) as file:
        file.write(content)


# TODO must return bytes
# def read(file_name:str, chunk_size:int = 2048):
#     byte_array = bytearray()
#     buffer     = None
#     with open(file = file_name, mode = _READ_BINARY) as file:
#         while True:
#             buffer = file.read(chunk_size)
#             if buffer:
#                 for byte in buffer:
#                     byte_array.append(byte)
#             else:
#                 break
#     return byte_array

def read(file_name:str, chunk_size:int = 2048):
    byt = None
    with open(file = file_name, mode = _READ_BINARY) as file:
        # READS all the bytes of the file 
        byt = file.read()
    return byt

def convert_bytearray_to_string(byte_array:bytearray):
    string = ""
    for byte in byte_array:
        string += chr(byte)
    return string


    
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


