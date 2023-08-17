import os
from urllib import request
import zipfile
from text_summary.logging import logger
from text_summary.utils.common import get_size
from text_summary.entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    
    def __init__(self,config : DataIngestionConfig):
        self.config = config

    def download_files(self):
        # if dataset doesn't downloaded yet 
        if not os.path.exists(self.config.local_data_file):
            filename , headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            # zip file is downloaded
            logger.info(f"File {filename} downloaded with the info : {headers}")
        else:
            # dataset is already downloaded
            logger.info(f"File {filename} is already exist of size : {get_size(Path(self.config.local_data_file))}")

    def extract_data(self):
        # extracts the zip file
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)