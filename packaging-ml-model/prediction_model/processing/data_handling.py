import os
import pandas as pd
import joblib
import logging
from prediction_model.config import config

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("data_handling")

# Load the datasets
def load_dataset(file_name):
    file_path = os.path.join(config.DATAPATH, file_name)
    _data = pd.read_csv(file_path)
    
    return _data

# Serialization
def save_pipeline_model(pipeline_to_save):
    save_model_path= os.path.join(config.SAVE_MODEL_PATH, config.MODEL_NAME)
    joblib.dump(pipeline_to_save, save_model_path)
    logger.info(f"Model has been saved as {config.MODEL_NAME} to {config.SAVE_MODEL_PATH}")

# Deserialization    
def load_pipeline_model(model_name):
    saved_model_path= os.path.join(config.SAVE_MODEL_PATH, model_name)
    model = joblib.load(saved_model_path)
    logger.info(f"Model loaded successfully as {model_name}")
    
    return model