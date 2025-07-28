import sys,os
import pickle
from src.logger import logging
from src.exception import CustomException
from src.utils import load_object


class PredictionPipeline:
    def __init__(self):
        try:
            self.model_path = os.path.join('artifacts', 'model.pkl')
            self.preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
        except Exception as e:
            logging.error("Error while getting model and preprocessor.")
            raise CustomException(e, sys)

    def predict(self,data):
        try:
            preprocessor = load_object(self.preprocessor_path)
            model = load_object(self.model_path)
            logging.info("Model and preprocessor loaded successfully.")
            
            # Transform the features
            transformed_data = preprocessor.transform(data)
            logging.info("Features transformed successfully.")

            # Make predictions
            pred = model.predict(transformed_data)
            logging.info("Prediction made successfully.")

            return pred

        except Exception as e:
            logging.error("Error occurred during prediction.")
            raise CustomException(e, sys)
