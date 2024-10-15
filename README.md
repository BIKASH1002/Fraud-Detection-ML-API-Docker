# Containerized Fraud Detection API: Leveraging ML and FastAPI

</div align = "justify">

This project is an end-to-end Machine Learning solution for detecting fraudulent transactions. The project includes a trained Machine Learning model, API integration using FastAPI and Containerization using Docker for deployment. The API allows users to input transaction details and get a fraud prediction based on the trained model.

# Content

1. [Overview](#overview)
  
2. [Setup](#setup)

3. [Procedure](#procedure)

4. [API Endpoints](#api-endpoints)
  
5. [Containerization](#containerization)

6. [Commands Summary](#commands-summary)

## Overview

This project uses Python, FastAP and Docker to provide a solution for predicting whether a financial transaction is fraudulent based on features like transaction type, amount and balances. The FastAPI application provides an easy-to-use interface where users can interact with the model and get predictions.

The project consists of the following main components:

- A **Machine Learning model** trained using scikit-learn to classify fraudulent transactions.

- An **API** developed using FastAPI for making predictions.

- **Containerization** of the application using Docker for easy deployment and environment consistency.

## Setup

- **Visual Studio Code:** for development

- **FastAPI:** model to API coversion

- **Docker:** for containerization

## Procedure

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

## API Endpoints

**GET `/`**

A simple endpoint to check if the API is running.

Following is the response from GET endpoint:

<div align = "center">
    <img src="https://github.com/user-attachments/assets/a8c88163-985b-4147-b313-2d8f073c0b32" alt="1" width="50%">
</div> 

**POST `/predict/`**

This is the main endpoint for fraud prediction. The GET and POST endpoints could be viewed interactively in Fast API Swagger UI.

<div align = "center">
    <img src="https://github.com/user-attachments/assets/8540dd37-da0d-4955-910c-977422701663" alt="1" width="50%">
</div>

Send a JSON payload with the transaction details and the API will return a prediction indicating whether the transaction is fraudulent.

<div align = "center">
    <img src="https://github.com/user-attachments/assets/8986625e-1986-417e-b65a-8c05c8e2e854" alt="1" width="50%">
</div>

Following is the response for testing trasaction values:

<div align = "center">
    <img src="https://github.com/user-attachments/assets/29cf866c-9585-454e-ac4b-8730bbcad11d" alt="1" width="50%">
</div>

## Containerization

- Create a dockerfile in the project repository defining the base image selection (lightweight Python image in our case), working directory, installing dependencies and exposing the ports.

- Start Docker Desktop, build the image and run the Docker container. After proper setup, the container can be viewed as follows:

<div align = "center">
    <img src="https://github.com/user-attachments/assets/be328612-258f-43bf-9d12-dcd4a4ec07ce" alt="1" width="50%">
</div>

- Do the container analysis to check the vulnerabilities. This can ve viewd as shown below: 

<div align = "center">
    <img src="https://github.com/user-attachments/assets/a5c42d7f-bf74-48f9-b310-d3b3ac86c716" alt="1" width="50%">
</div>

**NOTE:-** The critical vulnerability in above container is due to the fact that I have allowed parsing in the API. Since, I am not deploying it anywhere for general purpose, it is ok to ignore this vulnerability. But it's a good practice if we could incorporate token to access the API. 

## Commands Summary

**1. Run FastAPI:** uvicorn app.main:app --reload

**2. Checking API health status:** http://127.0.0.1:8000

**3. Checking FastAPI Swagger UI:** http://127.0.0.1:8000/docs#/

**4. Building Docker image:** docker build -t fraud_detection_api .

**5. Running Docker container:** docker run -d -p 8000:8000 fraud_detection_api

# Credits

**Kaggle:** for the dataset

**NOTE:-** Due to the large dataset, I have uploaded the chunk of the dataset in the repository. So to access the complete dataset, access it [here](https://www.kaggle.com/datasets/sriharshaeedala/financial-fraud-detection-dataset/data).

# Contributing

If you wouldd like to contribute to the project, feel free to fork the repository and submit a pull request. For any issues or feature requests, please open an issue on GitHub.

</div>

# License

This project is licensed under the MIT License. 

