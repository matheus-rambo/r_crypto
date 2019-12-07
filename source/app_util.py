# verifies a boolean string 
def convert_string_to_bool(string:str):
    if string.lower() in ("yes", "y", "true", "t", "1"):
        return True
    else:
        return False
    
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

    