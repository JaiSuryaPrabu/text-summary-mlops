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