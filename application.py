from flask import Flask, Response, render_template, request, session
import pandas as pd
import os, uuid
from src.pipelines.prediction_pipeline import PredictionPipeline
import sys
from src.logger import logging
from src.exception import CustomException
from src.utils import save_predictions
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.secret_key = os.environ.get('SECRET_KEY')

# Home page with form
@app.route('/')
def home():
    return render_template('index.html')

# Handle form submission
@app.route('/predict', methods=['POST'])
def predict():

    file = request.files.get('file')
    logging.info(f"File received from user for prediction {file.filename if file else 'None'}")
    print(file)
    # Check if a file is uploaded
    if file and file.filename.endswith('.csv'):
        df = pd.read_csv(file)
        logging.info(f"CSV file read successfully with shape {df.shape}")
        pip = PredictionPipeline()
        result = pip.predict(df)
        df['Exited'] = result
        print(f"Prediction result: {result}")
        print(f"DataFrame with predictions: {df.head()}")
        
        # Save DataFrame to a uniquely named CSV file 
        os.makedirs('temp', exist_ok=True)
        filename = f"prediction_result_{uuid.uuid4().hex}.csv"
        filepath = os.path.join("temp", filename)  # Make sure 'temp/' folder exists
        df.to_csv(filepath, index=False)
        session['predicted_file'] = filename
        logging.info(f"Predicted file saved as {filename} in temp directory")
        # Convert DataFrame to HTML for rendering
        df_html = df.to_html(classes='result-table', index=False)
        return render_template('result.html', table=df_html)
    else:
        data = {
            'CreditScore': [int(request.form['CreditScore'])],
            'Geography': [request.form['Geography']],
            'Gender': [request.form['Gender']],
            'Age': [int(request.form['Age'])],
            'Tenure': [int(request.form['Tenure'])],
            'Balance': [float(request.form['Balance'])],
            'NumOfProducts': [int(request.form['NumOfProducts'])],
            'HasCrCard': [int(request.form['HasCrCard'])],
            'IsActiveMember': [int(request.form['IsActiveMember'])],
            'EstimatedSalary': [float(request.form['EstimatedSalary'])],
            'Complain': [int(request.form['Complain'])],
            'Satisfaction Score': [int(request.form['Satisfaction Score'])],
            'Card Type': [request.form['Card Type']],
            'Point Earned': [int(request.form['Point Earned'])]
        }
        df = pd.DataFrame(data)

        # Make prediction using your pipeline
        predictor = PredictionPipeline()
        result = predictor.predict(df)
        print(f"Prediction result: {result}")
        logging.info(f"Prediction result: {result}")
        return render_template('result.html', prediction=result)

@app.route('/download')
def download():
    """Download the predicted CSV file."""

    filename = session.get('predicted_file')
    if not filename:
        return "No file available for download", 400

    filepath = os.path.join("temp", filename)
    if not os.path.exists(filepath):
        return "File not found", 404

    with open(filepath, "r") as f:
        csv_data = f.read()
    logging.info(f"CSV file {filename} read successfully for download")

    return Response(
        csv_data,
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=prediction_result.csv"}
    )


if __name__ == '__main__':
    app.run(debug=True, host=0.0.0.0)
