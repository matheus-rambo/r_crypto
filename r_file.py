def writeToFile(content:str, filename:str):
    file = open(filename, "ab+")
    file.write(content)
    file.close()

def openFile(filename:str):
    file = open(filename, "r")
    return file

def readFileLines(file):
    return file.read()