# Import required modules
import os
import sys
import logging
from pathlib import Path

# Infinite loop to get a non-empty project name from the user
while True:
    project_name = input("Enter your project name: ")
    if project_name != "":
        break

# Define a list of files and folders to create
list_of_files = [
    # Project Package Structure
    f"{project_name}/__init__.py",  # Create an __init__.py file inside the project root
    f"{project_name}/components/__init__.py",  # Create an __init__.py file inside 'components' subdirectory
    f"{project_name}/config/__init__.py",  # Create an __init__.py file inside 'config' subdirectory
    f"{project_name}/constants/__init__.py",  # Create an __init__.py file inside 'constants' subdirectory
    f"{project_name}/entity/__init__.py",  # Create an __init__.py file inside 'entity' subdirectory
    f"{project_name}/exception/__init__.py",  # Create an __init__.py file inside 'exception' subdirectory
    f"{project_name}/logger/__init__.py",  # Create an __init__.py file inside 'logger' subdirectory
    f"{project_name}/pipeline/__init__.py",  # Create an __init__.py file inside 'pipeline' subdirectory
    f"{project_name}/utils/__init__.py",  # Create an __init__.py file inside 'utils' subdirectory
    
    # Additional Files
    f"config/config.yaml",  # Create a 'config.yaml' file inside the project root
    "schema.yaml",  # Create a 'schema.yaml' file in the current directory
    "app.py",  # Create an 'app.py' file in the current directory
    "main.py",  # Create a 'main.py' file in the current directory
    "logs.py",  # Create a 'logs.py' file in the current directory
    "exception.py",  # Create an 'exception.py' file in the current directory
    "setup.py"  # Create a 'setup.py' file in the current directory
]

# Loop through the list of files and folders
for path in list_of_files:
    # Create a Path object for the current file/folder
    filepath = Path(path)
    
    # Split the path into directory and filename
    filedir, filename = os.path.split(filepath)
    
    # If the directory is not empty, create it if it doesn't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    
    # Create the file if it doesn't exist or if it's empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        logging.info(f"File is already present at : {filepath}")
