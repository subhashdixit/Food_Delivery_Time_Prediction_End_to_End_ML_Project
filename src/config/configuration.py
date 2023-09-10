# Write all the configuration code to connect all the variable
# Import necessary constants from an external module
from src.constants import *
import os, sys

# Set the root directory path using the previously defined ROOT_DIR_KEY
ROOT_DIR = ROOT_DIR_KEY

# Define the path to the dataset by joining the root directory, data directory, and data file key
DATASET_PATH = os.path.join(ROOT_DIR, DATA_DIR, DATA_DIR_KEY)
# This creates the complete path to the dataset file, ensuring easy access for processing.

# Define the path to the raw data file by joining relevant directory paths and the current timestamp
RAW_FILE_PATH = os.path.join(ROOT_DIR, ARTIFACT_DIR_KEY, DATA_INGESTION_KEY, CURRENT_TIME_STAMP,
                             DATA_INGESTION_RAW_DATA_DIR, RAW_DATA_DIR_KEY)
# This assembles the path to the raw data file, accounting for timestamp and directory structure.
# The raw data file is where unprocessed data will be stored before ingestion.

# Define the path to the training data file by joining relevant directory paths and the current timestamp
TRAIN_FILE_PATH = os.path.join(ROOT_DIR, ARTIFACT_DIR_KEY, DATA_INGESTION_KEY, CURRENT_TIME_STAMP,
                               DATA_INGESTION_INGESTED_DATA_DIR_KEY, TRAIN_DATA_DIR_KEY)
# This constructs the path to the training data file, considering timestamp and directories.
# The training data file is where preprocessed data will be stored after ingestion.

# Define the path to the test data file by joining relevant directory paths and the current timestamp
TEST_FILE_PATH = os.path.join(ROOT_DIR, ARTIFACT_DIR_KEY, DATA_INGESTION_KEY, CURRENT_TIME_STAMP,
                              DATA_INGESTION_INGESTED_DATA_DIR_KEY, TEST_DATA_DIR_KEY)
# This generates the path to the test data file, factoring in timestamp and directories.
# The test data file will contain preprocessed data for evaluation purposes.

