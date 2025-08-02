# Heart-Disease-Prediction-Web-App
This project is a machine learning-powered web application for predicting the likelihood of heart disease based on user input. It uses a trained DecisionTreeClassifier model and a Flask backend.

## Demo
![Demo of Heart Disease Prediction App]()


## Features
- User-friendly web interface for inputting patient data
- Predicts heart disease risk using a trained ML model
- Beautiful, modern UI with centered layout and styled Predict button

## How It Works
1. User enters patient details (age, sex, blood pressure, cholesterol, etc.)
2. The app processes the input and uses the ML model to predict heart disease risk
3. The result is displayed as "High Risk" or "Low Risk"

## Technologies Used
- Python
- Flask
- scikit-learn
- HTML/CSS
- Bootstrap (optional for further styling)

## Setup Instructions
1. Clone or download this repository
2. Place your trained model file (`model_dt1.pkl`) in the project root
3. Install required Python packages:
   ```bash
   pip install flask numpy scikit-learn
   ```
4. Run the app:
   ```bash
   python app.py
   ```
5. Open your browser and go to `http://localhost:5000`

## File Structure
- `app.py` : Flask backend and prediction logic
- `model_dt1.pkl` : Trained ML model
- `templates/index.html` : Main input form
- `templates/result.html` : Result display page
- `styles.css` : Custom styles (optional)

## Input Features
The form collects the following features:
- Age
- Sex
- Resting Blood Pressure
- Cholesterol
- Fasting Blood Sugar
- Max Heart Rate
- Exercise-Induced Angina
- OldPeak
- Number of Major Vessels
- Chest Pain Type (one-hot)
- Resting ECG (one-hot)
- ST Slope (one-hot)
- Thalium (one-hot)

## Output
- Displays whether the patient is at high or low risk of heart disease

## Author
- Ankit Kumar Singh

## License
This project is for educational purposes.
