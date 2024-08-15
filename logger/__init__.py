"""
"""

import datetime
import colorama
import inspect

from .utils import *
from .handler import *
from .error import *

class Logger:
    """"""
    def __init__(self, name: str, 
                       handler: BaseHandler, 
                       format: str = DEFAULT_FORMAT, 
                       level: int = Level.DEBUG, 
                       datefmt: str = DEFAULT_TIME_FORMAT, 
                       colored: bool = False,
                       shorten_levelname: bool = False):
        self._name = name
        self._format = format
        self._level = level
        self._handler = handler
        self._datefmt = datefmt
        self._colored = colored
        self._use_short_name = shorten_levelname
        
        if colored:
            self.levelname_meta = LevelNameMeta(
                format_blue("DEBUG" if not shorten_levelname else "D"),
                format_blue("INFO" if not shorten_levelname else "I"),
                format_yellow("WARNING" if not shorten_levelname else "W"),
                format_red("ERROR" if not shorten_levelname else "E"),
                format_red("CRITICAL" if not shorten_levelname else "C"),
            )
            
        else:
            self.levelname_meta = LevelNameMeta(
                "DEBUG" if not shorten_levelname else "D",
                "INFO" if not shorten_levelname else "I",
                "WARNING" if not shorten_levelname else "W",
                "ERROR" if not shorten_levelname else "E",
                "CRITICAL" if not shorten_levelname else "C",
                )
            
        self._configuration = {"name": self._name, 
                              "format": self._format, 
                              "level": self._level, 
                              "handler": self._handler, 
                              "datefmt": self._datefmt, 
                              "colored": self._colored, 
                              "shorten_levelname": self._use_short_name}
        
    @property
    def configuration(self):
        return self._configuration
    
    @property
    def name(self):
        return self._name
    
    @property
    def level(self):
        return self._level
    
    @property
    def handler(self):
        return self._handler
    
    @property
    def datefmt(self):
        return self._datefmt
    
    @property
    def colored(self):
        return self._colored
    
    @property
    def using_colored_level(self):
        return self.colored
    
    @property
    def is_colored(self):
        return self.colored
            
    def getChild(self, name: str, 
                       extend_configuration: bool = False, 
                       **kwargs):
        """Return a child logger with the specified name"""
        if not name.startswith(self.name):
            raise ValueError("The name of child logger must be started with father logger's name.")
        
        if extend_configuration:
            return __class__(name=name, **self.configuration)
        
        else:
            return __class__(name=name, **kwargs)
        
    def disable(self, level: int):
        """Disable the log under the specified level"""
        if level not in range(1, 6):
            raise ValueError("Invaild level")
        self._level = level
        
    getSubLogger = getChild
    
    def _format_text(self, level, message: str):
        """Format the text of the message"""
        current_namespace = getouterframe().f_code.co_name
        current_lineno = getouterframe().f_lineno
        current_filename = getouterframe().f_code.co_filename
        levelname = self.levelname_meta[level]
        
        return self._format.format(
            level=self.level,
            message=message,
            time=datetime.datetime.now().strftime(self.datefmt),
            asctime=datetime.datetime.now().strftime(self.datefmt),
            levelname=levelname, 
            funcname=current_namespace, 
            lineno=current_lineno,
            filename=current_filename, 
            name=self.name
        )
        
    def debug(self, message: str):
        """Log a debug message"""
        if self.level >= 1:
            return 
        return self.handler.handle(self._format_text(Level.DEBUG, message))
    
    def info(self, message: str):
        """Log an info message"""
        if self.level >= 2:
            return
        return self.handler.handle(self._format_text(Level.INFO, message))
    
    def warning(self, message: str):
        """Log a warning message"""
        if self.level >= 3:
            return
        return self.handler.handle(self._format_text(Level.WARNING, message))
    
    def error(self, message: str):
        """Log an error message"""
        if self.level >= 4:
            return
        return self.handler.handle(self._format_text(Level.ERROR, message))
    
    def critical(self, message: str):
        """Log a critical message"""
        if self.level >= 5:
            return
        return self.handler.handle(self._format_text(Level.CRITICAL, message))
    
    def reconfigure(self, **options):
        """
        Reconfigure the logger with the given options.

        This method allows you to change the configuration of the logger at runtime.
        You can pass in keyword arguments to change the following options:
        
            - colored: Whether to use colored level names (default: False)
            
            - datefmt: The format string for the date and time (default: DEFAULT_TIME_FORMAT)
            
            - format: The format string for the log messages (default: DEFAULT_FORMAT)
            
            - handler: The handler to use for logging (default: StdOutHandler)
            
            - level: The minimum level of messages to log (default: Level.NOTSET)
            
            - use_short_name: Whether to use short level names (default: False)

        Note that you cannot change the name of the logger using this method.
        """
        self._reconfigure(options)
        
    def _reconfigure(self, option_dict: dict):
        raise Deprecated("reconfigure", "1.0.0a1.post5", has_new=False)
          
rootLogger = Logger("root", 
                    handler=StdOutHandler(), 
                    level=Level.NOTSET)  

debug = rootLogger.debug
info = rootLogger.info
warning = rootLogger.warning
error = rootLogger.error
critical = rootLogger.critical

assert debug.__self__ is rootLogger

def getLogger(name: str, **options):
    """Get a logger with the given name and options"""
    return Logger(name, **options)

basicConfig = rootLogger.reconfigure
