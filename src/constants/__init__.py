# Define all the variable

import os, sys
from datetime import datetime

# Function to get the current timestamp in the format "YYYY-MM-DD HH-MM-SS"
def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}"

# Get the current timestamp and store it for labeling and organization
CURRENT_TIME_STAMP = get_current_time_stamp()

# Key for the root directory, using the current working directory
ROOT_DIR_KEY = os.getcwd()

# Directory name where data files are stored
DATA_DIR = "Data"
# Key for the specific data file ("finalTrain.csv" in this case)
DATA_DIR_KEY = "finalTrain.csv"
# Key for the directory to store project artifacts
ARTIFACT_DIR_KEY = "Artifact"
# Key for data ingestion related operations
DATA_INGESTION_KEY = "data_ingestion"
# Key for the raw data directory within the data ingestion
DATA_INGESTION_RAW_DATA_DIR = "raw_data_dir"
# Key for the directory where ingested data will be stored
DATA_INGESTION_INGESTED_DATA_DIR_KEY = "ingested_dir"
# Key for the raw data file name ("raw.csv" in this case)
RAW_DATA_DIR_KEY = "raw.csv"
# Key for the ingested training data file name ("train.csv" in this case)
TRAIN_DATA_DIR_KEY = "train.csv"
# Key for the ingested test data file name ("test.csv" in this case)
TEST_DATA_DIR_KEY = "test.csv"
