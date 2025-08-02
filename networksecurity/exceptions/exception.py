import sys
from networksecurity.logging import logger
class NetworkSecurityException(Exception):
    def __init__(self, error_msg,error_details:sys):
        self.error_msg=error_msg
        _,_,exec_tb=error_details.exc_info()

        self.lineno=exec_tb.tb_lineno
        self.file_name=exec_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error occured in python script name [{0}] line number [{1}] error_msg [{2}]".format(
            self.file_name,self.lineno, str(self.error_msg)
        )
    