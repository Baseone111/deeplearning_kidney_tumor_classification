import setuptools

with open("README.md","r", encoding="utf-8")as f:
    long_description = f.read()


__version__ = "0.0.0"


REPO_NAME = 'deeplearning_kidney_tumor_classification'
AUTHOR_USER_NAME = 'Baseone111'
SRC_REPO = 'cnnClassifier'
AUTHOR_EMAIL = 'opiofitson@gmail.com'



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='A small python package for deeplearning tasks',
    long_description=long_description,
    long_description_content= "text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",

    project_urls ={
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },

    package_dir={"": "src"},

    packages=setuptools.find_packages(where="src")
    
)