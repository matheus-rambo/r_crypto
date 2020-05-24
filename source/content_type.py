from enum import Enum

class ContentType(Enum):
    
    TEXT      = ('text')
    FILE      = ('file')
    DIRECTORY = ('directory')

    def __init__(self, type_str:str):
        self._type = type_str