from dataclasses import dataclass
from pathlib import Path

# STAGE 1 : data ingestion
@dataclass(frozen=True)
class DataIngestionConfig:
    # contents in the config/config.yaml file
    root_dir : Path 
    source_URL : str 
    local_data_file : Path
    unzip_dir : Path

# STAGE 2 : data validation
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir : Path
    STATUS_FILE : str
    ALL_REQUIRED_FILES : list

# STAGE 3: data transformation
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir : Path
    data_path : Path
    tokenizer_name : Path

# STAGE 4: model trainer
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir : Path
    data_path : Path
    model_ckpt : Path
    num_of_epochs : int
    warmup_steps : int
    per_device_train_batch_size : int
    weight_decay : float
    logging_steps : int
    evaluation_strategy : str 
    eval_steps : int
    save_steps : float
    gradient_accumulation_steps : int