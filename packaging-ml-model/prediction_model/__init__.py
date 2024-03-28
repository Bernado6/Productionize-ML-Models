import os
from prediction_model.config import config
with open(os.path.join(config.PACKAGE_ROOT,  'VERSION'), encoding='utf-8') as f:
    VERSION = f.read().strip()

__version__ = VERSION
"""The version of this package."""