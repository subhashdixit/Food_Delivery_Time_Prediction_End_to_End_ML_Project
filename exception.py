# Import the necessary modules from Flask framework and custom-defined modules
from flask import Flask
from src.logger import logging  # Import the logging module from src.logger
from src.exception import CustomException  # Import the CustomException class from src.exception
import os, sys  # Import the os and sys modules

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL ("/") and specify accepted methods
@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        # Simulate an intentional exception for testing purposes
        raise Exception("we are testing our Exception file")  # Error
    except Exception as e:
        # Create a CustomException instance to handle and format the caught exception
        ML = CustomException(e, sys)
        # Log the formatted error message using the logging module
        logging.info(ML.error_message)

        # Log a testing message for the logging functionality
        logging.info("We are testing our logging file")

        # Return a response string
        return "End to End Machine Learning"

# Check if this script is being run directly (not imported as a module)
if __name__ == "__main__":
    # Start the Flask development server with debugging enabled on port 5000
    app.run(debug=True)  # 5000
