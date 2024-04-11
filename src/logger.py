"""
Overall, this code sets up a logging system that writes log messages to a file in a directory named "logs", with each log file named based
 on the current date and time. It's a basic setup, but it can be expanded upon by adding more configuration options or customizing the log format as needed.
"""
import logging #module provides a flexible framework for emitting log messages
import os #module provides a way to interact with the operating system, such as creating directories and joining file paths.
from datetime import datetime #provides classes for manipulating dates and times.

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #generates a log file name based on the current date and time using datetime.now().
#The strftime method formats the current date and time 
"""
os.getcwd(): This function returns the current working directory.
os.path.join(): This function joins one or more path components intelligently. In this case, it's used to create a path to the "logs" directory and the log file.
os.makedirs(): This function creates a directory and its parent directories if they don't exist. The exist_ok=True parameter ensures that no exception is raised if the directory already exists

"""
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE) #creates the full path to the log file by joining the logs directory path with the log file name.
"""
logging.basicConfig(): This function configures the logging system. It's used to set up the default handler for logging messages.
filename: This specifies the file where log messages will be written. In this case, it's set to the full path of the log file.
format: This specifies the format of the log messages. It's a string that can contain various placeholders, such as asctime (the time of the log message),
 levelname (the level of the log message), message (the log message itself), etc.
level: This specifies the minimum severity level for log messages to be written to the file. In this case, it's set to INFO, which means that all log
 messages with severity level INFO or higher will be written to the file.
"""
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)
if __name__=="__main__":
    logging.info("Logging has started")
   