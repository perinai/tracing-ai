# AI-Powered Health Monitoring System (from Tracing AI)

This project, completed as part of the AI for Software Engineering course, is an AI-powered system that analyzes health metrics to detect anomalies and provide personalized recommendations.

## Overview

The system is a Python-based web application built with the Flask framework. It uses a machine learning model (Random Forest) trained on simulated health data to predict whether a user's vital signs (heart rate, blood oxygen) are normal or anomalous. The entire application is containerized using Docker, making it portable, scalable, and easy to deploy.

## Key Features

*   **AI-Powered Anomaly Detection:** Uses a scikit-learn model to classify health data in real-time.
*   **User-Friendly Web Interface:** A simple HTML form allows users to input their metrics and receive instant feedback.
*   **Containerized with Docker:** The entire application is packaged into a Docker image, ensuring it runs consistently in any environment.
*   **Developed in the Cloud:** The project was developed and containerized entirely within GitHub Codespaces, demonstrating modern cloud-based development workflows.

## How to Run This Project

To run this application, you must have Docker installed on your machine.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-github-username/tracing-ai.git
    ```
    *(**Important:** Replace `your-github-username` with your actual GitHub username!)*

2.  **Navigate into the project directory:**
    ```bash
    cd tracing-ai
    ```

3.  **Build the Docker image:**
    ```bash
    docker build -t tracing-ai-app .
    ```

4.  **Run the Docker container:**
    ```bash
    docker run -p 5000:5000 tracing-ai-app
    ```

5.  **Access the application:**
    Open your web browser and go to `http://localhost:5000`.

## Project Structure

├── Dockerfile # Defines the application container
├── requirements.txt # Lists the Python dependencies
├── app.py # The main Flask application logic
├── health_monitor_model.pkl # The trained AI model
├── model_features.pkl # The feature list for the model
└── templates/
├── index.html # The user input form
└── result.html # The results display page
