# Containerized Fraud Detection API: Leveraging ML and FastAPI

This project is an end-to-end Machine Learning solution for detecting fraudulent transactions. The project includes a trained Machine Learning model, API integration using FastAPI and Containerization using Docker for deployment. The API allows users to input transaction details and get a fraud prediction based on the trained model.

# Table of Contents

1. Overview
  
2. Setup

3. Procedure

4. API Endpoints
  
5. Dockerization

# Overview

This project uses Python, FastAP and Docker to provide a solution for predicting whether a financial transaction is fraudulent based on features like transaction type, amount and balances. The FastAPI application provides an easy-to-use interface where users can interact with the model and get predictions.

The project consists of the following main components:

- A **Machine Learning model** trained using scikit-learn to classify fraudulent transactions.

- An **API** developed using FastAPI for making predictions.

- **Containerization** of the application using Docker for easy deployment and environment consistency.

# Setup

- **Visual Studio Code:** for development

- **FastAPI:** model to API coversion

- **Docker:** for containerization

# Procedure

To implement this work, follow the steps below to build, run and deploy the Fraud Detection API:

**1. Data Preparation:**

- Start by loading and exploring the dataset, ensuring it is clean and structured for training a machine learning model.

- Preprocess the data by handling missing values, normalizing numerical features and encoding categorical features using techniques like one-hot encoding.

**2. Model Training:**

- Choose an appropriate machine learning algorithm (e.g., Random Forest) for fraud detection.

- Train the model on the preprocessed dataset and evaluate its performance using metrics like accuracy and precision.

- Save the trained model to a file (e.g., using joblib or pickle) for later use in the FastAPI application.

**3. API Development:**

- Set up a FastAPI project to create a RESTful API for fraud detection.

- Define endpoints such as a health check endpoint (GET /) to ensure the API is running and a prediction endpoint (POST /predict/) to accept transaction details and return a fraud prediction.

- Load the trained model within the FastAPI application to make predictions based on user inputs.

**4. Testing the API:**

- Run the FastAPI server locally and test the API endpoints using Swagger UI which automatically documents and provides an interface for testing the API.

- Ensure that the API returns correct predictions based on sample transaction data.

**5. Dockerization:**

- Dockerize the FastAPI application by creating a Dockerfile that includes the necessary dependencies and environment to run the API in an isolated container.

- Build the Docker image and run the container to ensure that the API functions correctly in a containerized environment.

**6. Vulnerability Check:**

- Analyze the Docker image for vulnerabilities using a scanning tool to identify potential security risks.

- Address any critical vulnerabilities by updating the base image or dependencies to safer versions.

This procedure outlines the key steps to take the project from data preparation to deployment, ensuring a structured and secure solution for fraud detection.
