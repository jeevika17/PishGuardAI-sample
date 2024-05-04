from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
from tensorflow import keras
from Feature_Extractor import extract_features

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Path to the trained model
model_path = r"C:\Users\Jeevika\OneDrive\Desktop\phishing\Phishing-Attack-Domain-Detection\models\Malicious_URL_Prediction.h5"

# Load the model
print("Loading the model...")
model = keras.models.load_model(model_path)
print("Model loaded successfully.")

# Define a route to handle POST requests to '/analyze-url'
@app.route('/analyze-url', methods=['POST'])
def analyze_url():
    # Get the URL from the request data
    data = request.json
    url = data.get('url')

    # Extract features from the URL
    print("Extracting features from URL...")
    url_features = extract_features(url)
    url_features = np.array([url_features])

    # Make prediction
    print("Making prediction...")
    prediction = model.predict(url_features)
    probability = prediction[0][0] * 100
    probability = round(probability, 3)

    # Return the prediction result as JSON
    return jsonify({
        'url': url,
        'result': probability
    })

if __name__ == '__main__':
    app.run(debug=True)
