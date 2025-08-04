from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
import sys,os

from dataclasses import dataclass
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException
from src.utils import save_object

# Data transformation configuration
@dataclass
class DataTransformationConfig:
    preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')

# Data transformation class to handle preprocessing of data
class DataTransformation:
    def __init__(self):
        self.transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        
        try:
            trf = ColumnTransformer([
                ('encode', OneHotEncoder(sparse_output=False, handle_unknown='ignore'),[1,2,12])
                ], remainder='passthrough')
            logging.info("Data transformer object created successfully.")
            logging.info(f"Transformer details: {trf}")
            return trf
        except Exception as e:
            logging.error("Error occurred in data_transformer_object method.")
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Data read successfully from train and test paths.")
            logging.info(f"Train data shape: {train_df.shape}, Test data shape: {test_df.shape}")

            # separate features and target variable
        
            target_column_name = 'Exited'
            X_train =  train_df.drop(columns=['RowNumber', 'CustomerId', 'Surname', target_column_name], axis=1)
            y_train = train_df[target_column_name]
            X_test = test_df.drop(columns=['RowNumber', 'CustomerId', 'Surname', target_column_name], axis=1)
            y_test = test_df[target_column_name]
            logging.info("Separated features and target variable.")

            # get the data transformer object
            transform_obj = self.get_data_transformer_object()
            
            # fit and transform the training data
            X_train_transformed = transform_obj.fit_transform(X_train)
            # transform the test data
            X_test_transformed = transform_obj.transform(X_test)
            logging.info("Train and Test data transformed successfully.")


            save_object(
                file_path = self.transformation_config.preprocessor_path,
                obj = transform_obj
            )
            logging.info("Preprocessor pickle is created and saved")

            return (
                X_train_transformed, X_test_transformed, y_train, y_test,
            )
        except Exception as e:
            logging("Error occured in initiate_data_transformation method")
            raise CustomException(e, sys)
