Assignment Solutioning.

1. Provided entire training codebase in training_notebook.ipynb
2. Inference code script is available at inference.py
3. CNN Model is saved inside model directory.
4. Test inference images are provided inside  test_data directory
5. Dockerfile is attached which can be build using the command : docker build -t mnist-inference -f Dockerfile.dockerfile .
6. Run the docker using command: docker run -p 5000:5000 mnist-inference
7. Curl to test locally : curl -X POST -F "image=@test_data/three.jpg" http://localhost:5000/predict
8. Attached the screenshot "curl request.png" of the tested curl on test_images.
