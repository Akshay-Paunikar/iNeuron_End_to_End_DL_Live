import os
import sys
from src.cnnClassifier.logger import logging
from src.cnnClassifier.exception import CustomException

def divide(x:int, y:int) -> int:
    result = x / y
    return result

try:
    divide(5,0)
    logging.info("divide operation successful")
except Exception as e:
    logging.info("Error occured please check the error message")
    raise CustomException(e,sys)
