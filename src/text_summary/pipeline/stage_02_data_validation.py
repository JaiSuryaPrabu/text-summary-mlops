# imports
from text_summary.config.configuration import ConfigurationManager
from text_summary.components.data_validation import DataValidation

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        configManager = ConfigurationManager()
        data_val_config = configManager.get_data_validation_config()
        data_validation = DataValidation(data_val_config)
        data_validation.validate_all_file_exist()