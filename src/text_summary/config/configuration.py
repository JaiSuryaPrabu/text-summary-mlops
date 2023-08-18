from text_summary.constants import *
from text_summary.utils.common import read_yaml,create_directories
from text_summary.entity import DataIngestionConfig,DataValidationConfig

# CONGIF MANAGER
class ConfigurationManager:
    def __init__(self,config_path=CONFIG_FILE_PATH,params_path=PARAMS_FILE_PATH):
        # reading the yaml files
        self.config = read_yaml(config_path)
        self.param = read_yaml(params_path)

        # create directories
        create_directories([self.config.artifacts_root])

    # STAGE 1
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir= config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
    
    # STAGE 2
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir    = config.root_dir,
            STATUS_FILE = config.STATUS_FILE,
            ALL_REQUIRED_FILES=config.ALL_REQUIRED_FILES      
        )

        return data_validation_config