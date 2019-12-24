# writes text content to a file
# Note that the parameter 'wt' overwrites the content if the file exists    
# 'wt' means Writes Text, it is the same as just 'w'
def write(file_name:str, content:str, extension:str):
    # if the user defined a extension, we will remove it and then add our extension
    if '.' in file_name:
        index = file.rindex('.')
        file_name = file_name[0:index]
    file_name = file_name + extension
    with open(file_name, 'wt') as file:
        file.write(content)


# rt means Read Text
def read_file_content(file_name:str, buffer_size:int, charset: str = 'utf-8'):
    content = ""
    data = -1
    position = 0
    with open(file_name, 'rt', encoding=charset) as file:
        while data != "":
            data = file.read(buffer_size) 
            position = position + buffer_size
            file.seek(position)
            content = content + data
    return content
    
def read_data_from_console(message: str, show_input: bool = False):
    if show_input:
        return input(message)
    else:
        from getpass import getpass
        return getpass(message)

def get_file_extension(file_name: str):
    last_index = file_name.rindex('.')
    return file_name[last_index:] 