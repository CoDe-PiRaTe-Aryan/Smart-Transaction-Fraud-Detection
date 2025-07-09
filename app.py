from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import numpy as np
import pickle
import os

app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)

# Load model and scaler
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/guide')
def guide():
    return send_from_directory(app.static_folder, 'guide.html')

@app.route('/dashboard')
def dashboard():
    return send_from_directory(app.static_folder, 'dashboard.html')

@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory(app.static_folder, path)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        features = np.array(data['features']).reshape(1, -1)
        features_scaled = scaler.transform(features)
        prediction = model.predict(features_scaled)[0]
        result = "fraud" if prediction == 1 else "safe"

        # Explaination (mock)
        explanation = (
            "⚠️ High amount and zero balance left → Suspicious"
            if result == "fraud"
            else "✅ Normal transaction pattern detected"
        )

        return jsonify({'result': result, 'explanation': explanation})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
