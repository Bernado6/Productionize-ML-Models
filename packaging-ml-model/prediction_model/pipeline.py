from sklearn.pipeline import Pipeline
from prediction_model.config import config
import numpy as np
from prediction_model.processing.preprocessing import (
    DomainProcessing,
    MeanImputer,
    ModeImputer,
    LogTransforms,
    DropColumns,
    CustomLabelEncoder)

from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression

classification_pipeline = Pipeline(
    [
        ("DomainProcessing", DomainProcessing(
                                               variable_to_modify=config.FEATURE_TO_MODIFY,
                                               variable_to_add=config.FEATURE_TO_ADD)),
        
        ('Mean Imputation', MeanImputer(variables=config.NUM_FEATURES)),
        ('Mode Imputation', ModeImputer(variables=config.CAT_FEATURES)),
        ("Dropping Columns", DropColumns(variables_to_drop=config.DROPPED_FEATURE)),
        ('Label Encoding', CustomLabelEncoder(variables=config.FEATURES_TO_ENCODE)),
        ('Log Transformation', LogTransforms(variables=config.LOG_TRANSFORM_FEATURES)),
        ('MinMaxScale', MinMaxScaler()),
        ('Logistic Regresssion', LogisticRegression(random_state=0))
    ]
)