import logging
import os
from datetime import datetime

LOG_DIR = "logs"
logfile_name = f'{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log'
log_path = os.path.join(os.getcwd(), LOG_DIR)
os.makedirs(log_path, exist_ok=True)
LOG_FILE = os.path.join(log_path, logfile_name)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)

"""
def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
        logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger
"""