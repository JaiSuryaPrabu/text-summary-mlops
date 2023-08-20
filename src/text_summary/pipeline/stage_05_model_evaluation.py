from text_summary.components.model_evaluation import ModelEvaluation
from text_summary.config.configuration import ConfigurationManager

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        configManager = ConfigurationManager()
        model_eval_config = configManager.get_model_eval_config()
        model_eval = ModelEvaluation(model_eval_config)
        model_eval.evaluate()