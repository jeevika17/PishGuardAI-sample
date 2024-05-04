import numpy as np
from tensorflow import keras
from Feature_Extractor import extract_features


# ------------------------------------------------------------------------

# This function takes the url and returns probability value

def get_prediction(url, model_path):
    print("Loading the model...")
    model = keras.models.load_model(model_path)

    # Extract features from the URL
    print("Extracting features from url...")
    url_features = extract_features(url)
    print(type(url_features))  # Ensure that url_features is a list
    print(url_features)

    # Convert url_features to a numpy array
    url_features = np.array([url_features])
    print(type(url_features))  # Ensure that url_features is now a numpy array
    print(url_features)

    # Make prediction
    print("Making prediction...")
    prediction = model.predict(url_features)
    print("Prediction:", prediction)
    # Rest of your code...
    i = prediction[0][0] * 100
    i = round(i,3)
    print("There is ",i,"% chance,the url is malicious !")

    return i