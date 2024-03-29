import pandas as pd 
import logging
import numpy as np
from prediction_model.config import config
from prediction_model.processing.data_handling import load_pipeline_model, load_dataset


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("Predict")

classification_pipeline = load_pipeline_model(config.MODEL_NAME)

def make_pred(data_input):
    data =pd.DataFrame(data_input)
    pred = classification_pipeline.predict(data[config.FEATURES])
    output = np.where(pred == 1,'Y', 'N')
    print(f"Output=====: {output}")
    results = {'predictions': output}
    logger.info(type(f"Type of Output:  {type(results)}")) 
    return results


# Testing
# def make_pred():
#     test_data =load_dataset(config.TEST_FILE)
#     pred = classification_pipeline.predict(test_data[config.FEATURES])
#     output = np.where(pred == 1,'Y', 'N')
#     return output
# if __name__=="__main__":
#     make_pred()
    