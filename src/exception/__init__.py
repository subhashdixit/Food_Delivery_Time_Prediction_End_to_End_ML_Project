import os, sys  # Import the os and sys modules

# Define a custom exception class that inherits from the built-in Exception class
class CustomException(Exception):
    def __init__(self, error_message: Exception, error_detailes: sys):
        # Initialize the error_message attribute with the detailed error message
        self.error_message = CustomException.get_detailed_error_message(error_message=error_message,
                                                                        error_detailes=error_detailes)
        
    # A static method to create a detailed error message
    @staticmethod
    def get_detailed_error_message(error_message: Exception, error_detailes: sys) -> str:
        # Get the exception traceback using sys.exc_info()
        _, _, exce_tb = error_detailes.exc_info()

        # Get line numbers and file name associated with the exception
        exception_block_line_number = exce_tb.tb_frame.f_lineno
        try_block_line_number = exce_tb.tb_lineno
        file_name = exce_tb.tb_frame.f_code.co_filename

        # Construct the error message with file name, line numbers, and original error message
        error_message = f"""
        Error occurred in execution of:
        [{file_name}] at
        try block line number: [{try_block_line_number}]
        and exception block line number: [{exception_block_line_number}]
        error message: [{error_message}]
        """
        return error_message
    
    # Override the __str__ method to return the error_message attribute as a string
    def __str__(self):
        return self.error_message
    
    # Override the __repr__ method to return the name of the CustomException class as a string
    def __repr__(self):
        return CustomException.__name__.str()
