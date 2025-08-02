import re
from flask import Flask, render_template, request
import numpy as np
import pickle
import math as math

app = Flask(__name__)  # Initialize Flask app
model = pickle.load(open('model_dt1.pkl', 'rb'))  # Load the heart disease prediction model
if isinstance(model, tuple):
    model = model[0]  # Unpack model if loaded as a tuple

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')  # Render the home page

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Retrieve all 23 input features from the form (matching form names)
        feature_names = [
            'Age', 'Sex', 'RestingBloodPressure', 'Cholesterol', 'FastingBloodSugar',
            'MaxHeartRate', 'ExerciseInducedAngina', 'OldPeak', 'nMajorVessels',
            'ChestPain_0', 'ChestPain_1', 'ChestPain_2', 'ChestPain_3',
            'RestingECG_0', 'RestingECG_1', 'RestingECG_2',
            'STSlope_0', 'STSlope_1', 'STSlope_2',
            'Thalium_0', 'Thalium_1', 'Thalium_2', 'Thalium_3'
        ]
        values = [float(request.form[name]) for name in feature_names]
        values = np.array([values])
        prediction = model.predict(values)
        return render_template('result.html', prediction=int(prediction[0]))  # Show result

if __name__ == '__main__':
    app.run(debug=True)
