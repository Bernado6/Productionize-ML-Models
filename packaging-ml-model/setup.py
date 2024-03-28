import io
import os
from pathlib import Path
from setuptools import setup, find_packages

# Metadata of Package
NAME = "prediction_model"
DESCRIPTION = "Loan Prediction Model"
URL = "https://github.com/Bernado6/Productionize-ML-Models"
EMAIL = "benardkipngenoyegon@gmail.com"
AUTHOR = "Bernard Kipngeno"
REQUIRES_PYTHON = ">=3.9.13"


PWD = os.path.abspath(os.path.dirname(__file__))

# Get the list of packages to be installed
def list_requirements(f_name='requirements.txt'):
    with io.open(os.path.join(PWD, f_name), encoding="utf-8") as file:
        return file.read().splitlines()
    
try:
    with io.open(os.path.join(PWD, 'README.md'), encoding="utf-8") as file:
        long_description = '\n' + file.read()
        
except FileNotFoundError:
    long_description = DESCRIPTION
    
# load the package's __version__.py module as dictionary
ROOT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_DIR/ NAME
about = {}

with open(PACKAGE_DIR, 'VERSION') as f:
    _version = f.read().strip()
    about['__version__']= _version
        

setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages= find_packages(exclude = ('tests',)),
    install_requires=list_requirements(),
    package_data={
        'prediction_model':    ['VERSION']},
    extras_require = {},
    license="MIT License",
    include_package_data=True,
    classifiers=[
        'License :: OSI Approved :: MIT License'
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: Cpython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
    # zip_safe=False,
    # project_urls={
        # "Source": URL,
    # },
    
    )