# Import necessary libraries and modules.
from src.constants import *  # Import constants from a predefined module.
from src.config.configuration import *  # Import configurations from a predefined module.
import os, sys  # Import the 'os' and 'sys' modules for file and system operations.
import pandas as pd  # Import the 'pandas' library for data manipulation.
import numpy as np  # Import the 'numpy' library for numerical operations.
from sklearn.model_selection import train_test_split  # Import train_test_split from scikit-learn for data splitting.
from dataclasses import dataclass  # Import dataclass decorator for creating structured classes.
from src.logger import logging  # Import logging functionality from a predefined module.
from src.exception import CustomException  # Import a custom exception class.
# from src.components.data_transformation import DataTransformation, DataTransformationConfig  # Import data transformation classes from a predefined module.

# Define a dataclass for configuration related to data ingestion.
@dataclass
class DataIngestionConfig:
    train_data_path: str = TRAIN_FILE_PATH  # Set default paths for training data.
    test_data_path: str = TEST_FILE_PATH  # Set default paths for test data.
    raw_data_path: str = RAW_FILE_PATH  # Set default paths for raw data.

# Define a class for data ingestion.
class DataIngestion:
    def __init__(self):
        # Initialize the data ingestion configuration using the DataIngestionConfig class.
        self.data_ingestion_config = DataIngestionConfig()

    # Method to initiate the data ingestion process.
    def iniitiate_data_ingestion(self):
        try:
            # Read data from a CSV file defined by DATASET_PATH.
            df = pd.read_csv(DATASET_PATH)

            # Create directories for saving raw data if they don't exist.
            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path), exist_ok=True)

            # Save the raw data to the specified path.
            df.to_csv(self.data_ingestion_config.raw_data_path, index=False)

            # Split the data into training and test sets.
            train_set, test_set = train_test_split(df, test_size=0.20, random_state=42)

            # Create directories for saving training and test data if they don't exist.
            os.makedirs(os.path.dirname(self.data_ingestion_config.train_data_path), exist_ok=True)
            os.makedirs(os.path.dirname(self.data_ingestion_config.test_data_path), exist_ok=True)

            # Save the training and test data to the specified paths.
            train_set.to_csv(self.data_ingestion_config.train_data_path, header=True)
            test_set.to_csv(self.data_ingestion_config.test_data_path, header=True)

            # Return the paths to the training and test data.
            return (
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path
            )

        # Handle exceptions and raise a custom exception with the error message.
        except Exception as e:
            raise CustomException(e, sys)

# Entry point of the script.
if __name__ == "__main__":
    # Create an instance of the DataIngestion class.
    obj = DataIngestion()
    # Initiate the data ingestion process and get the paths to training and test data.
    train_data_path, test_data_path = obj.iniitiate_data_ingestion()
 
    # # Create an instance of the DataTransformation class for further data processing.
    # data_transformation = DataTransformation()
    # # Initiate the data transformation process using the paths to training and test data.
    # train_arr, test_arr, _ = data_transformation.inititate_data_transformation(train_data_path, test_data_path)
