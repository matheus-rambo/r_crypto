from getpass import getpass

class IOUtil():
    
    def __init__(self, show_input:bool):
        self.show_input = show_input

    def stdin(self, message:str):
        if self.show_input:
            return input(message)
        return getpass(message)

    def stdin_to_bytes(self, message:str, charset:str = 'utf-8'):
        return self.stdin(message).encode(charset)

    def read_ask_answear(self, message:str, acceptable_answear:chr = 'y'):
        answear = self.stdin(message)
        return False if ( answear is None or answear.strip() == '' ) else answear.lower()[0] == acceptable_answear

    def stdout(self, message:str, parameters:dict = None):
        if parameters is not None:
            print(message.format(**parameters))
        else:
            print(message)