import os
import sys
from logger import logging
from exception import CustomException

import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit

from dataclasses import dataclass


# Initialize the data ingestion config

@dataclass
class DataIngestionConfig():
    data_get_path = os.path.join('notebooks', 'Customer-Churn-Records.csv')
    train_data_path = os.path.join('artifacts', 'train.csv')
    test_data_path = os.path.join('artifacts', 'test.csv')

# Data Ingestion class to handle data retrieval and processing
class DataIngestion:    
    def __init__(self):
        self.ingestion_conf = DataIngestionConfig()

    def get_data(self):

        try:
            if self.ingestion_conf.data_get_path:
                df = pd.read_csv(self.ingestion_conf.data_get_path)
                logging.info("Read data as csv file.")
                logging.info(f"Shape of the data: {df.shape}")
            else:
                logging.info("Path not exists ", self.ingestion_conf.data_get_path)
        except CustomException as e:
            logging.info("Error while reading the data.")
            raise CustomException(e, sys)
        
        # for splitting the data
        try:
            if df is not None:
                logging.info("Splitting the data into train and test sets.")
                sss = StratifiedShuffleSplit(n_splits=1,test_size=0.2)
                
                X = df.drop('Exited', axis=1)
                y = df['Exited']

                for train_idx,test_idx in sss.split(X,y):
                    X_train, X_test = X.iloc[train_idx], X.iloc[test_idx]
                    y_train, y_test = y.iloc[train_idx], y.iloc[test_idx]
                
                train_set = pd.concat([X_train, y_train], axis=1)
                test_set = pd.concat([X_test, y_test], axis=1)
                logging.info(f"Train set shape: {train_set.shape}, Test set shape: {test_set.shape}")
                

                # Create directories if they do not exist
                try:
                    os.makedirs(os.path.dirname(self.ingestion_conf.train_data_path), exist_ok=True)
                    logging.info(f"Directories created successfully at {self.ingestion_conf.train_data_path}")
                except Exception as e:
                    logging.info("Error while creating directories.")
                    raise CustomException(e, sys)

                # Save the split data
                logging.info("Saving train and test data to CSV files.")
                train_set.to_csv(self.ingestion_conf.train_data_path, index=False)
                test_set.to_csv(self.ingestion_conf.test_data_path, index=False)
                
                logging.info("Train and test data saved successfully.")
                logging.info(f"Train data path: {self.ingestion_conf.train_data_path}")
                logging.info(f"Test data path: {self.ingestion_conf.test_data_path}")
                
                # Return the paths of the saved data
                return (
                    self.ingestion_conf.train_data_path,
                    self.ingestion_conf.test_data_path
                )

            else:
                logging.info("DataFrame is None, cannot split data.")
        except CustomException as e:
            logging.info("Error while splitting the data.")
            raise CustomException(e, sys)
        
