# Dockerized Flask Application
This repository contains a simple Flask application dockerized for easy deployment. The Dockerfile provided sets up a Python environment, installs Flask, and runs the Flask application inside a Docker container.

Prerequisites
Before running the application, ensure you have the following installed:

1. Docker: Install Docker

2. Build the Docker Image
Navigate to the project directory and build the Docker image:
cd your-repository
docker build -t my-flask-app .

3. Run the Docker Container
Run the Docker container using the following command:
docker run -d --name my-container -p 5000:5000 my-flask-app


4. Run the Docker Container
Run the Docker container using the following command:
docker run -d --name my-container -p 5000:5000 my-flask-app

4. Access the Application
Once the container is running, you can access the Flask application in your web browser at http://localhost:5000.

5. Stop and Remove the Container
When you're done testing the application, you can stop and remove the Docker container:
docker stop my-container
docker rm my-container


