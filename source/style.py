from enum import Enum 

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
    UNDERLINE = '\033[04m