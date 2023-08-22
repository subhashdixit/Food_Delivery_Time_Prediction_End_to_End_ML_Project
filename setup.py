"""
To use the project as a package or a library, the 'setup.py' script is being used for future purposes.
Definition: This script is used to capture essential information such as the project's name, version, and dependencies. It's a module commonly utilized to build and distribute Python packages.

Import necessary functions and modules:
"""
from setuptools import setup, find_packages
from typing import List

# Define various project-related constants
PROJECT_NAME = 'Food Delivery Time Prediction'
VERSION = "0.0.1"
DESCRIPTION = "End to End Food Delivery Time Prediction Machine Learning Project"
AUTHOR_NAME = "Subhash Dixit"
AUTHOR_EMAIL = "subhashdixit17@gmail.com"

REQUIREMENTS_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements_list() -> List[str]:
    """
    Retrieve a list of project dependencies from a requirements file.

    Reads the contents of the 'requirements.txt' file, removes newline characters,
    and handles the case where the file contains the '-e .' (editable mode) entry.
    Returns a list of cleaned requirement names.

    Returns:
        List[str]: A list of project dependency names.
    """
    # Open the requirements file and read its lines
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()

        # Remove newline characters from each requirement name
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]

        # Handle the case where '-e .' is present (editable mode entry)
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)

        return requirement_list

# Setup configuration for the project package
setup(
    name=PROJECT_NAME,          # Name of the project
    version=VERSION,            # Version of the project
    description=DESCRIPTION,    # Description of the project
    author=AUTHOR_NAME,         # Author's name
    author_email=AUTHOR_EMAIL,  # Author's email
    packages=find_packages(),   # Automatically find all packages by looking for '__init__.py' files in the 'src' folder
    install_requirements=get_requirements_list()  # Retrieve project dependencies from a requirement file
)
