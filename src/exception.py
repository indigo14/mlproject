import sys #often used for accessing command-line arguments, file I/O functionality, and error handling.
import logging #module provides a flexible framework for emitting log messages
#from src.logger import logging

"""error_detail: holds the result of sys.exc_info(),
    a tuple containing information about the current exception being handled. sys.exc_info() returns a 
    tuple in the form (type, value, traceback)."""

def error_message_detail(error, error_detail:sys):#error= error object, error_detail= a type hint  indicates that error_detail is expected to be of type 'sys'
    
    """ 
    exc_tb is a traceback object obtained from sys.exc_info(), and tb_frame is an attribute of the traceback object that refers to the frame object 
    at the top of the call stack when the exception occurred.
    """
    _,_,exc_tb=error_detail.exc_info()
    """
    tb_frame: This attribute of the traceback object refers to the frame object at the top of the call stack when the exception occurred.
     the frame object contains information about the execution frame, including the code object.
    f_code, This code object contains information about the bytecode being executed, including the filename, line numbers, and function name.
    co_filename he filename where the code associated with the frame was loaded from
    """
    file_name=exc_tb.tb_frame.f_code.co_filename #extracts the filename from the code object associated with the traceback.
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))
    """
    file_name: contains the filename where the exception occurred. It was obtained from the frame object associated
    with the traceback. 
    exc_tb.tb_lineno: This attribute represents the line number in the file where the exception occurred. It is 
    extracted from the traceback object. 
    str(error): This converts the error object to a string representation. The error variable 
    likely holds an instance of an exception class representing the error that occurred.
      By converting it to a string, you get a human-readable 
    representation of the error message.
    """
     
    return error_message

"""
This code defines a custom exception class named CustomException that inherits from Python's built-in Exception class
This line defines the constructor method (__init__) for the CustomException class. The __init__ method is called when an instance of the class is created.
self: This parameter represents the instance of the  It's used to access variables and methods within the class.
error_message: This parameter is used to specify the error message associated with the exception.
 When an instance of CustomException is created, you can pass an error message to this parameter.
error_detail: sys: This parameter is a type hint specifying that the error_detail parameter is expected to be of type sys. Type hints provide information about the expected types of function parameters and return values.
"""



class CustomException(Exception): #defines a new class named CustomException, which is a subclass of the built-in Exception class
    def __init__(self, error_message, error_detail:sys): #the constructor method (__init__) for the CustomException class. The __init__ method is called when an instance of the class is created.
        """
        This line calls the constructor of the base class (Exception) using the super() function. It passes the error_message parameter
          to the constructor of the base class. The error_message parameter is expected to contain the error message provided when an 
          instance of CustomException is created.
        """
        super().__init__(self.error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
    
