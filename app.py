from src.end_to_end_data_science_project.logger import logging
from src.end_to_end_data_science_project.exception import CustomException
import sys

if __name__=="__main__":
    logging.info("The execution has started")

    try:
        a = 1

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys.exc_info())
