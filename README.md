**Assignment Solution Overview**

**Training Codebase**: The complete training codebase is provided in the training_notebook.ipynb notebook, ensuring transparency and reproducibility in model training.

**Inference Code Script**: An inference script named inference.py is available, facilitating model inference on new data.

**CNN Model:** The trained CNN model is stored within the model directory, ensuring easy access and deployment.

**Test Inference Images**: Test inference images are conveniently placed inside the test_data directory, aiding in the validation and evaluation of the model.

**Flask API Script:** The main Flask API script, app.py, orchestrates the model predictions by invoking the utility script predict.py from a URL and delivers JSON output.

**Dockerfile:** A Dockerfile is provided for containerization. Building the Docker image is straightforward using the command: docker build -t mnist-inference -f Dockerfile.dockerfile.

**Running the Docker Container:** The Docker container can be executed using the command: docker run -p 5000:5000 mnist-inference, ensuring seamless deployment and scalability.

**Testing Locally with cURL:** Testing the API locally is simplified with cURL. Utilize the command curl -X POST -F "image=@test_data/three.jpg" http://localhost:5000/predict to validate predictions on test images.

**Validation Screenshot:** A screenshot titled "curl request.png" showcasing the successful execution of the cURL command on test images is included, ensuring clarity and validation of the process.

This comprehensive solution ensures a professional and efficient workflow for training, deploying, and testing the MNIST digit recognition model.
