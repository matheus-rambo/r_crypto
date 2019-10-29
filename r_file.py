def write_to_file(content:str, filename:str):
    file = open(filename, "ab+")
    file.write(content)
    file.close()

def open_file(filename:str):
    file = open(filename, "r")
    return file

def read_file_lines(file):
    return file.read()