# Import required modules
import logging
import os
import sys
from datetime import datetime

# Define the directory for log files
LOG_DIR = "logs"
LOG_DIR = os.path.join(os.getcwd(), LOG_DIR)

# Create the log directory if it doesn't exist
os.makedirs(LOG_DIR, exist_ok=True)

# Generate a timestamp for the log file name using the current date and time
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
file_name = f"log_{CURRENT_TIME_STAMP}.log"
# Example output file: log_2023-07-23-22-34-38.log

# Create the full path for the log file
log_file_path = os.path.join(LOG_DIR, file_name)

# Configure the logging settings
logging.basicConfig(
    filename=log_file_path,
    filemode="w",  # Create a new log file every time
    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',  # Log message format
    level=logging.INFO  # Set logging level to INFO
)

# Detailed explanation of the code:
# The provided code sets up a logging mechanism that generates log files with a timestamp in their names.
# It uses the `logging` module to handle the logging process.

# 1. LOG_DIR Creation:
#    - The script defines the directory path where log files will be stored as "logs".
#    - The `os.path.join()` function combines the current working directory with "logs".

# 2. Directory Creation:
#    - The script creates the log directory using `os.makedirs()` with `exist_ok=True` to avoid errors if the directory already exists.

# 3. Generating Timestamp:
#    - The current date and time are obtained using `datetime.now().strftime('%Y-%m-%d-%H-%M-%S')`.
#    - This timestamp is formatted as "YYYY-MM-DD-HH-MM-SS".

# 4. Log File Name:
#    - The log file name is generated with the format "log_<timestamp>.log".

# 5. Log File Path:
#    - The full path for the log file is created by joining the log directory path and the log file name.

# 6. Logging Configuration:
#    - The `logging.basicConfig()` function is used to configure the logging settings.
#    - `filename` is set to the `log_file_path`, indicating where log messages will be written.
#    - `filemode` is set to "w" to create a new log file with each run.
#    - `format` specifies the format of log messages, including the timestamp, logger name, log level, and the log message itself.
#    - `level` is set to `logging.INFO`, indicating that messages with INFO level and higher will be recorded in the log.

# Overall, this code sets up a logging system that creates timestamped log files in a specified directory, and it configures the logging format and level for those log files.
