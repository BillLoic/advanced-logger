from types import FrameType
import colorama
from enum import Enum
from dataclasses import dataclass

def format_red(txt):
    return colorama.Fore.RED + txt + colorama.Style.RESET_ALL

def format_blue(txt):
    return colorama.Fore.BLUE + txt + colorama.Style.RESET_ALL

def format_white(txt):
    return colorama.Fore.WHITE + txt + colorama.Style.RESET_ALL

def format_yellow(txt):
    return colorama.Fore.YELLOW + txt + colorama.Style.RESET_ALL

class Level():
    NOTSET = 0
    DEBUG = 1
    INFO = 2
    WARNING = 3
    ERROR = 4
    CRITICAL = 5
    
@dataclass
class LevelNameMeta:
    debug_txt: str
    info_txt: str
    warning_txt: str
    error_txt: str
    critical_txt: str
    def __getitem__(self, k):
        match k:
            case 1:
                return self.debug_txt
            case 2:
                return self.info_txt
            case 3:
                return self.warning_txt
            case 4:
                return self.error_txt
            case 5:
                return self.critical_txt
            case _:
                raise

DEFAULT_FORMAT = "{name}:{levelname}:{message}"
DEFAULT_TIME_FORMAT = r"%Y/%m/%d %H:%M:%S.%f"
VAILD_KEY = [
    "name", 
    "levelname", 
    "asctime", 
    "time", 
    "lineno", 
    "message", 
    "funcname", 
    "filename"
]

def getouterframe() -> FrameType:
    import inspect
    return inspect.currentframe().f_back.f_back.f_back