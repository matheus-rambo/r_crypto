def write_to_file(content:str, filename:str):
    file = open(filename, "ab+")
    file.write(content.decode("utf-8").encode("utf-8"))
    file.close()

def open_file(filename:str):
    file = open(filename, "r", encoding='utf-8')
    return file

def read_file_lines(file):
    return file.read()