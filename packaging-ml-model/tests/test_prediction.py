import pytest
from prediction_model.config import config
from prediction_model.processing.data_handling import load_dataset
from prediction_model.predict import make_pred

@pytest.fixture
def single_prediction():
    test_data = load_dataset(config.TEST_FILE)
    single_row = test_data[:1]
    result = make_pred(single_row)
    
    return result

def test_single_pred_not_none(single_prediction):
    assert single_prediction is not None
    
def test_single_pred_str(single_prediction):
    assert isinstance(single_prediction.get('predictions')[0], str)
    
def test_single_pred_validate(single_prediction):
    assert  single_prediction.get('predictions')[0] == 'Y'