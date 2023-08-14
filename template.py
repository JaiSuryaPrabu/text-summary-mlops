'''template.py is a py script to manage the template of the project'''

# imports
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(message)s",datefmt="%d-%b-%y %H:%M:%S")

project_name = "text_summary"

# list of files to be created when this template file is executed
files_list = [
    ".github/workflows/.gitkeep", # for cd/ci operations
    f"src/{project_name}/__init__.py", # constructor of the project folder
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "congif/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb"
]

# creating the folders and files
for filepath in files_list:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)

    # creating directories
    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating {filedir}/ directory for {filename} file")
    
    # creating file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            # creates the file
            pass
        logging.info(f"Creating empty file : {filename}")

    else:
        logging.info(f"Filename : {filename} does exists")