# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /MNIST

RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt into the container at /MNIST
COPY requirements.txt .

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire contents of the current directory into the container at /MNIST
COPY . /MNIST

# Expose the port the MNIST runs on
EXPOSE 5000

# Define environment variable
ENV MODEL_PATH /MNIST/model/mnist_cnn_model.h5
ENV TEST_IMAGE /MNIST/test_data/three.jpg

# Run inference.py when the container launches
CMD ["python", "app.py"]
