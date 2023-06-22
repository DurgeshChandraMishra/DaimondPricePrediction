import os,sys
import numpy as np
import pandas as pd
import pickle
from src.logger import logging
from src.exception import CustomException

def save_object(file_path,obj):

    try :
        os.makedirs(os.path.dirname(file_path),exist_ok=True)

        with open(file_path, 'wb') as f :
            pickle.dump(obj,f)

    except Exception as e:
        raise CustomException(e,sys)