'''setup.py is used for pypi package '''
import setuptools

with open("README.md","r") as f:
    long_description = f.read()

version = "0.0.1"

REPO_NAME = "text-summary-mlops"
AUTHOR_USER_NAME = "JaiSuryaPrabu"
SRC_REPO = "Text Summarization"
AUTHOR_EMAIL = "jaisuryap25204@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=version,
    long_description=long_description,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A MLOPS project based on text summarization",
    long_description_content="text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir= {"":"src"},
    packages= setuptools.find_packages(where="src")
)