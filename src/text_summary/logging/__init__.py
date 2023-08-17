# imports
import os
import logging
import sys

logging_str = "[%(asctime)s : %(levelname)s : %(module)s : %(message)s]"

# create the log file
log_dir = "logs"
log_filepath = os.path.join(log_dir,"runnning_logs.log")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level = logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath), # to log in a file
        logging.StreamHandler(sys.stdout) # to show it in a terminal
    ]
)

logger = logging.getLogger("textSummaryLogger")