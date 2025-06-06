# app.py

from flask import Flask, request, render_template
import pandas as pd
import joblib

app = Flask(__name__)

# Load the trained model and features
model = joblib.load('health_monitor_model.pkl')
model_features = joblib.load('model_features.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    user_input = {
        'heart_rate': [float(request.form['heart_rate'])],
        'blood_oxygen': [float(request.form['blood_oxygen'])],
        'activity_level_running': [1 if request.form['activity_level'] == 'running' else 0],
        'activity_level_walking': [1 if request.form['activity_level'] == 'walking' else 0]
    }
    input_df = pd.DataFrame(user_input)
    final_df = input_df.reindex(columns=model_features, fill_value=0)

    prediction = model.predict(final_df)[0]
    proba = model.predict_proba(final_df)[0]

    if prediction == 1:
        status, status_class = "Anomaly Detected", "anomaly"
        recommendation = f"Warning: Metrics are unusual (Confidence: {proba[1]*100:.0f}%). Consider resting."
    else:
        status, status_class = "Normal", "normal"
        recommendation = f"Metrics appear normal (Confidence: {proba[0]*100:.0f}%). Keep it up!"

    return render_template('result.html', status=status, recommendation=recommendation, status_class=status_class)

if __name__ == '__main__':
    app.run(debug=True)