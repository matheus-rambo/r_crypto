from source.app_constants import READ_BINARY, WRITE_BINARY

class File():

    def __init__(self, filename:str, charset: str = 'utf-8', chunk_size:int = None):
        self.filename   = filename
        self.chunk_size = chunk_size
        self.charset    = charset

    def read(self):
        byte_array = bytearray()
        buffer     = None
        with open(file = self.filename, mode = READ_BINARY ) as file:        
            while True:
                buffer = file.read(self.chunk_size)
                if buffer:
                    for byte in buffer:
                        byte_array.append(byte)
                else:
                    break
        return bytes(byte_array)

    def read_content_to_json(self):
        content = self.read()
        from json import loads
        return loads(content.decode(self.charset))
    
    def _replace_to_extension(self, extension:str) -> str:
        last_dot_index = -1 if self.filename.find('.') < 0 else self.filename.rindex('.')
        if last_dot_index >= 0:
            return self.filename[:last_dot_index] + extension
        else:
            return self.filename + extension

    def write(self, content:bytes, extension:str = None):
        filename = self.filename if not extension else self._replace_to_extension(extension)
        with open(file = filename, mode = WRITE_BINARY ) as file:
            file.write(content)