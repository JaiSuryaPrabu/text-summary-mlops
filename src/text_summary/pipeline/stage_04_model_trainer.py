from text_summary.config.configuration import ConfigurationManager
from text_summary.components.model_trainer import ModelTrainer

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(model_config)
        model_trainer.train()