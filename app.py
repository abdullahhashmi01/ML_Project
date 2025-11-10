import sys
from src.Mlproject.exception import CustomException
from src.Mlproject.logger import logging

try:
    logging.info("Application started")
    
    # Your actual application code goes here
    # Example:
    # model = load_model()
    # data = preprocess_data()
    # predictions = model.predict(data)
    
    # Remove or comment out this line that was causing the error:
    # a = 1 / 0  # This was causing ZeroDivisionError
    
    logging.info("Application completed successfully")
    
except Exception as e:
    logging.error("An error occurred in the application")
    raise CustomException(e, sys)