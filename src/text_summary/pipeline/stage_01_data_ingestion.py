from text_summary.config.configuration import ConfigurationManager
from text_summary.components.data_ingestion import DataIngestion

class DataIngestionTrainingPipeline:

    def __init__(self):
        configManager = ConfigurationManager()
        data_ingestion_config = configManager.get_data_ingestion_config()
        data_ingestion = DataIngestion(config = data_ingestion_config)
        data_ingestion.download_files()
        data_ingestion.extract_data()