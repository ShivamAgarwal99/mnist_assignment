import numpy as np
from tensorflow.keras.models import load_model
import cv2

# Load the saved model
model = load_model("model/mnist_cnn_model.h5")

# Function to preprocess input image
def preprocess_image(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Resize the image to 28x28
    resized = cv2.resize(gray, (28, 28))
    # Normalize pixel values to be between 0 and 1
    image = resized / 255.0
    # Reshape image to add a channel dimension
    image = np.expand_dims(image, axis=-1)
    # Add batch dimension
    image = np.expand_dims(image, axis=0)
    return image

# Function to make predictions
def predict_image(image):
    preprocessed_image = preprocess_image(image)
    # Make prediction
    prediction = model.predict(preprocessed_image)
    # Get predicted class label
    predicted_class = np.argmax(prediction)
    return predicted_class

input_image = cv2.imread("test_data/three.jpg") 
predicted_class = predict_image(input_image)
print("Predicted class:", predicted_class)
