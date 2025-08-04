import os,sys
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException

from sklearn.linear_model import LogisticRegression
from src.utils import save_object, evaluate_model
from dataclasses import dataclass


# Create Model trainer config
@dataclass
class ModelTrainerConfig:
    trained_model_path = os.path.join("artifacts", "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def model_train(self,X_train,X_test,y_train,y_test):
        clf = LogisticRegression(solver="newton-cholesky")
        try:
            clf.fit(X_train, y_train)
            logging.info("Model trained successfully.")
        
            # Evaluate the model
            choice = int(input("Now, you are going to evaluate the model.\n" \
            "1 for test data. \n" \
            "2 for train data itself. "))
            if choice == 1:
                score = evaluate_model(clf, X_test, y_test)
                print(f"Test data evaluation score: {score}")
            elif choice == 2:
                score = evaluate_model(clf, X_train, y_train)
                print(f"Train data evaluation score: {score}")
            else:
                logging.error("Invalid choice.")
                raise CustomException("Invalid choice.", sys)
            # Save the trained model
            save_object(
                file_path=self.model_trainer_config.trained_model_path,
                obj=clf
            )
            logging.info("Trained model saved successfully as pickle file.")

        except Exception as e:
            logging.error("Error occurred in model_train method.")
            raise CustomException(e, sys)