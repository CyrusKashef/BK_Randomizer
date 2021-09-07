import logging
from logging.handlers import RotatingFileHandler
import os

def create_logger(developer_mode):
    logger = logging.getLogger("Rotating Log")
    if(developer_mode):
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
    FORMAT = '[%(levelname)s] %(asctime)-15s - %(funcName)s: %(message)s'
    handler = RotatingFileHandler(os.getcwd() + "\Randomizer_Log_File.log", maxBytes=(512*1024), backupCount=1)
    logger.addHandler(handler)
    logging.basicConfig(format=FORMAT)
    return logger