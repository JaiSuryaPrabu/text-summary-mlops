
# imports
from text_summary.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from text_summary.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
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