'''common.py is used to call functions that are frequently used'''

# imports
import os
from box.exceptions import BoxValueError
import yaml
from text_summary.logging import logger
from ensure import ensure_annotations
from box import ConfigBox # alt to dict()
from pathlib import Path
from typing import Any

# ensure_annotations will check the datatype passed to the functions
@ensure_annotations
def read_yaml(path_to_yaml : Path) -> ConfigBox:
    '''
    reads yaml file and returns ConfigBox

    Args:
        path_to_yaml(str) : Path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type 
    '''
    try:
        with open(path_to_yaml,"r") as file:
            content = yaml.safe_load(file)
            logger.info(f"YAML file `{path_to_yaml}` loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"YAML file `{path_to_yaml}` is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_dirs : list ,can_log = True):
    '''
    creates list of directories

    Args:
    path_to_dirs (list) : list of path of directories
    can_log (bool) : To enable or disable the logging for creating the directories
    '''
    for path in path_to_dirs:
        os.makedirs(path,exist_ok=True)
        if can_log:
            logger.info(f"`{path}` Directory is created ")

@ensure_annotations
def get_size(path : Path) -> str:
    '''
    returns the size of file
    
    Args:
        path (str) : Path like input

    Returns:
        str : size in KB
    '''
    size = round(os.path.getsize(path)/1024)
    return f" ~ {size} KB"
