from enum                 import Enum 
from source.app_constants import WINDOWS_OS

class Background(Enum):

    BLACK     ='\033[40m'
    RED       ='\033[41m'
    GREEN     ='\033[42m'
    ORANGE    ='\033[43m'
    BLUE      ='\033[44m'
    PURPLE    ='\033[45m'
    CYAN      ='\033[46m'
    LIGHTGREY ='\033[47m'

class Foreground(Enum):

    BLACK      ='\033[30m'
    RED        ='\033[31m'
    GREEN      ='\033[32m'
    ORANGE     ='\033[33m'
    BLUE       ='\033[34m'
    PURPLE     ='\033[35m'
    CYAN       ='\033[36m'
    LIGHTGREY  ='\033[37m'
    DARKGREY   ='\033[90m'
    LIGHTRED   ='\033[91m'
    LIGHTGREEN ='\033[92m'
    YELLOW     ='\033[93m'
    LIGHTBLUE  ='\033[94m'
    PINK       ='\033[95m'
    LIGHTCYAN  ='\033[96m'

class Atributes(Enum):

    RESET     = '\033[0m'
    BOLD      = '\033[01m'
    UNDERLINE = '\033[04m'

class Formatter():

    def __init__(self):
        from platform import system
        if system() == WINDOWS_OS:
            import os 
            # enable colors in prompt
            os.system('color')

    def _format_foreground(self, foreground: Foreground, string:str) -> str:
        return '{}{}{}'.format(foreground.value, string, Atributes.RESET.value)

    def green_foreground(self, string:str) -> str:
        return self._format_foreground(Foreground.GREEN, string)
    
    def red_foreground(self, string:str) -> str: 
        return self._format_foreground(Foreground.RED, string)

    @staticmethod
    def yellow_foreground(string:str) -> str: 
        return Formatter._format_foreground(Foreground.YELLOW, string)

    @staticmethod
    def purple_foreground(string:str) -> str: 
        return Formatter._format_foreground(Foreground.PURPLE, string)