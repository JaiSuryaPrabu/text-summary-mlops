# Text Summary
Implementation of basic nlp text summarization task in complete end to end ML project.

## Steps
1. Create `template.py` to create the structure of the project
2. Create a python virtual environment specifically for this project
3. Write the required packages in `requirements.txt`

| Package Name | Usage |
| ------------ | ----- |
| transformers | Pretrained Models |
| transformers[sentencepiece] | Unsupervised Text tokenizer and detokenizer |
| datasets | For efficient data preprocessing and public datasets |
| rouge-score | Evaluating the auto gen text with human produced summary |
| py7zr | to compress , decompress , encrypt and decrypt |
| pandas | To work with **tabulated** data |
| nltk | Text processing library for *classification,tokenization,stemming,...* |
| tqdm | Produce progress bar in for loop |
| PyYAML | YAML parcer and emitter |
| matplotlib | Produce static , animated , visualization | 
| torch | DL library |
| notebook | Jupyter notebook environment |
| boto3 | AWS Software Development Toolkit |
| mypy-boto3-s3 | Type annotation for boto3 |
| python-box | Replacement for `dict()` datatype |
| ensure | An assertion helper |
| fastapi | Web framework for bulding API |
| uvicorn | ASGI *(Asynchronous Server Gateway Interface)* web server for python |
| jinja2 | Template engine |

4. Writing code in `logging/__init__.py`
5. Writing code in `utils/common.py` 
6. Work on the `research/*.ipynb` files for training and saving the model
7. Working on the **WORKFLOW**:
    0. Upload the *dataset* in the public cloud like `github`
    1. Update the `config/config.yaml`
    2. Update the `params.yaml`
    3. Update the `entity` and define the **dataclassess**
    4. Update the `src/constants/`
    5. Update the `src/config/configuration.py`
    6. Update the `src/components`
    7. Update the `src/pipeline`
    8. Update the `main.py`
    9. Update the `app.py`
