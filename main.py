
# imports
from text_summary.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from text_summary.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from text_summary.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from text_summary.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from text_summary.logging import logger

# Stage 1 : Data Ingestion
STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f"~~~ {STAGE_NAME} is started ~~~")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"~~~ {STAGE_NAME} is completed ~~~")
except Exception as e:
    logger.exception(e)
    raise e

# STAGE 2 : Data Validation
STAGE_NAME = "Data Validation stage"
try:
    logger.info(f"~~~ {STAGE_NAME} started ~~~")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"~~~ {STAGE_NAME} completed ~~~")
except Exception as e:
    logger.exception(e)
    raise e

# STAGE 3 : Data Transformation
STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f"~~~ {STAGE_NAME} started ~~~")
    data_validation = DataTransformationTrainingPipeline()
    data_validation.main()
    logger.info(f"~~~ {STAGE_NAME} completed ~~~")
except Exception as e:
    logger.exception(e)
    raise e

# STAGE $ : Model Trainer
STAGE_NAME = "Model Trainer stage"
try:
    logger.info(f"~~~ {STAGE_NAME} started ~~~")
    data_validation = ModelTrainerPipeline()
    data_validation.main()
    logger.info(f"~~~ {STAGE_NAME} completed ~~~")
except Exception as e:
    logger.exception(e)
    raise e