import os
from text_summary.logging import logger
from text_summary.config.configuration import DataValidationConfig

class DataValidation:
    def __init__(self,config : DataValidationConfig):
        self.config = config

    def validate_all_file_exist(self) -> bool:
        try :
            validation_status = None

            all_files = os.listdir(os.path.join("artifacts","data_ingestion","samsum_dataset"))

            for file in all_files:
                if file in self.config.ALL_REQUIRED_FILES:
                    # required file is found
                    validation_status = True
                else:
                    # file not found
                    validation_status = False
                with open(self.config.STATUS_FILE,"a") as f:
                    f.write(f"File name : `{file}` status : {validation_status} \n")
            return validation_status
        except Exception as e:
            raise e