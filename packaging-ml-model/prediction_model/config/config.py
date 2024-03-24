import pathlib
import os
import prediction_model

PACKAGE_ROOT = pathlib.Path(prediction_model.__file__).resolve().parent

DATAPATH = os.path.join(PACKAGE_ROOT, "datasets")

TRAIN_FILE = "train.csv"
TEST_FILE = "test.csv"
SAVE_MODEL_PATH = os.path.join(PACKAGE_ROOT, "trained_models")

#  Target variable
TARGET = "Loan_Status"
# Feature Engineering Parameters/Model parameters
FEATURES = ['Gender', 'Married', 'Dependents', 'Education',
       'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
       'Loan_Amount_Term', 'Credit_History', 'Property_Area']

NUM_FEATURES = ['ApplicantIncome', 'LoanAmount', 'Loan_Amount_Term']

CAT_FEATURES = ['Gender', 'Married', 'Dependents', 'Education',
                'Self_Employed', 'Property_Area','Credit_History']
# fEATURES TO ENCODE
FEATURES_TO_ENCODE = ['Gender', 'Married', 'Dependents', 'Education',
                      'Self_Employed', 'Property_Area','Credit_History']


FEATURE_TO_MODIFY = ['ApplicantIncome']

FEATURE_TO_ADD = 'CoapplicantIncome'

DROPPED_FEATURE =['CoapplicantIncome']

MODEL_NAME = "loan_classification_model.pkl"

LOG_TRANSFORM_FEATURES = ['ApplicantIncome', 'LoanAmount', 'Loan_Amount_Term']

# SUBMISSION_TEMPLATE = "submission_template.csv"
# MODEL_PIPELINE = "pipeline.pkl"

# # Model Evaluation Metrics
# METRICS = {
#     "accuracy": "Accuracy",
#     "precision": "Precision",
#     "recall": "Recall",
# }

# # Data Preprocessing Constants
# DEFAULT_ENCODING = "utf-8"
# CSV_DELIMITER = ";"
# HEADERS = False
# HAS_LABEL = True

# # Model Training Constants      
# N_JOBS = -1       # Use all available cores for parallel processing (-1 means use all)
# CV_SPLITTER = None     # Use the default KFold splitter (random state is set to 42 by   