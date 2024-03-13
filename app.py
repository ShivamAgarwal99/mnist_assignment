from flask import Flask, request, jsonify
import numpy as np
from tensorflow.keras.models import load_model
import os
import cv2

app = Flask(__name__)

# Load the saved model
model = load_model(os.environ["MODEL_PATH"])

# Function to preprocess input image
def preprocess_image(image):
    
    resized = cv2.resize(image, (28, 28))
    # Normalize pixel values to be between 0 and 1
    image = resized / 255.0
    # Reshape image to add a channel dimension
    image = np.expand_dims(image, axis=-1)
    # Add batch dimension
    image = np.expand_dims(image, axis=0)
    return image

# Function to make predictions
def predict_image(image):
    # Make prediction
    prediction = model.predict(image)
    # Get predicted class label
    predicted_class = np.argmax(prediction)
    return predicted_class

@app.route('/predict', methods=['POST'])
def predict():
    # Get the image from the POST request
    image_file = request.files['image']
    image = cv2.imdecode(np.frombuffer(image_file.read(), dtype=np.uint8), cv2.IMREAD_UNCHANGED)
    # Preprocess the image
    preprocessed_image = preprocess_image(image)
    # Make prediction
    predicted_class = predict_image(preprocessed_image)
    # Return the prediction as JSON
    return jsonify({'prediction': int(predicted_class)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
