from text_summary.config.configuration import ConfigurationManager
from text_summary.components.data_transformation import DataTransformation

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        configurationManagaer = ConfigurationManager()
        data_transformation_config = configurationManagaer.get_data_transformation_config()
        data_transformation = DataTransformation(data_transformation_config)
        data_transformation.convert()