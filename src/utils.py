import sys,os
import pickle
import pandas as pd
import numpy as np
from src.logger import logging
from src.exception import CustomException
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import cross_val_score


def save_object(file_path, obj):
    """Saves an object to a file using pickle."""

    try:

        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file:
            pickle.dump(obj, file)
        logging.info(f"Object saved successfully at {file_path}")
    
    except Exception as e:
        logging.error(f"Error occurred while saving object at {file_path}")
        raise CustomException(e, sys)
    
def evaluate_model(model, X, y):
    """Evaluates the model using accuracy score."""
    
    try:
        y_pred = model.predict(X)
        accuracy = accuracy_score(y, y_pred)
        logging.info(f"Model accuracy: {accuracy}")

        user = input("You want Cross validation?")
        if user.lower() == 'yes':
            n = int(input("Enter number of folds for cross validation: "))
            cv_scores = cross_val_score(model, X, y, cv=n)
            print(f"Cross validation scores: {cv_scores}")
            print(f"Mean cross validation score: {np.mean(cv_scores)}")
            logging.info("Cross validation is complete.")
        else:
            logging.info("Skipping cross validation.")
        return accuracy
    
    except Exception as e:
        logging.error("Error occurred while evaluating the model.")
        raise CustomException(e, sys)

def load_object(file_path):
    """Loads an object from a file using pickle."""
    try:
        with open(file_path, 'rb') as file:
            obj = pickle.load(file)
        logging.info(f"Object loaded successfully from {file_path}")
        return obj
    
    except Exception as e:
        logging.error(f"Error occurred while loading object from {file_path}")
        raise CustomException(e, sys)


def save_predictions(file_path, obj):
    """Saves predictions to a file."""
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        obj.to_csv(file_path, index=False)
        logging.info(f"Prediction saved successfully at {file_path}")
    
    except Exception as e:
        logging.error(f"Error occurred while saving predictions at {file_path}")
        raise CustomException(e, sys)


