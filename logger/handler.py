import smtplib
import sys
import io
from logger.error import *

class BaseHandler:
    
    def __init__(self):
        self.handle_method = lambda _: None
        
    def handle(self, text):
        raise NotImplementedError("You should override this method.")
    
class IOHandler(BaseHandler):
    """
    A handler class pipe message into a writable stream.
    """
    def __init__(self, ioobj: io.StringIO | io.TextIOWrapper | io.BufferedWriter):
        self.ioobj = ioobj
        self.handle_method = self.ioobj.write
        
    def handle(self, text):
        self.handle_method(text + "\n")
        
class FileHandler(IOHandler):
    """
    A handler class pipe message into a file.
    """
    def __init__(self, filename: str, encoding: str = "utf-8"):
        super().__init__(io.open(filename, 'w', encoding=encoding))
        
class FileObjectHandler(IOHandler):
    """
    A handler class pipe message into a file object.
    """
    def __init__(self, fileobj: io.BufferedWriter):
        super().__init__(fileobj)
        
class StringIOHandler(IOHandler):
    """
    A handler class pipe message into a StringIO object
    """
    def __init__(self, stream: None | io.StringIO):
        if stream is None:
            stream = io.StringIO()
            super().__init__(stream)
        else:
            super().__init__(stream)
            
class StdOutHandler(FileObjectHandler):
    """
    A handler class pipe message into the standard output.
    """
    def __init__(self):
        super().__init__(sys.stdout)
        
class FunctionHandler(BaseHandler):
    """
    A handler class pipe message into a function.
    """
    def __init__(self, func: callable):
        self.handle_method = func
        
class SMTPHandler(BaseHandler):
    """
    A handler class pipe message into an SMTP server.
    """
    def __init__(self, smtp_instance: smtplib.SMTP | smtplib.SMTP_SSL):
        raise WillBeAddInNewerVersion("SMTPHandler", "1.1.0")
        self.smtp = smtp_instance
        self.handle_method = self.smtp.send
