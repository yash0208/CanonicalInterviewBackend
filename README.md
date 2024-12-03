# Canonical Interview Web Application

## Overview

Hi, I’m Yash! To showcase my skills in microservices architecture, Docker containerization, and DevOps practices, I’ve built this dynamic web application. The frontend is crafted with HTML and JavaScript, while the backend is powered by Python Flask, split into two microservices. These services fetch technical questions from Firebase (NoSQL) and non-technical questions from Supabase (SQL). The backend is containerized with Docker, and deployment is automated using a CI/CD pipeline with GitHub Actions, running seamlessly on AWS EC2. This project demonstrates my expertise in modern development and cloud integration.

## Features

- **RESTful API**:
  - Fetch technical questions from Supabase.
  - Fetch non-technical questions from Firebase.
  - Welcome route for basic health checks.
- **Cloud Integration**:
  - **Supabase** for storing technical questions.
  - **Firebase** for managing non-technical questions.
- **CI/CD Pipeline**:
  - GitHub Actions for automated build and deployment.
  - Deployment to AWS EC2 using Docker.

## Project Structure

```plaintext
.
├── Dockerfile            # Docker configuration for containerizing the app
├── requirements.txt      # Python dependencies
├── app.py                # Main entry point for the Flask application
├── api_gateway/          # Blueprint for API Gateway
│   ├── api_gateway.py    # API routes and logic
│   └── __init__.py       # Initialization
├── firebase_config/      # Firebase integration
│   ├── firebase_client.py
│   └── __init__.py
├── supabase_config/      # Supabase integration
│   ├── supabase_client.py
│   └── __init__.py
├── models/               # Data models
│   ├── question_answer.py
│   └── __init__.py
├── .github/workflows/    # CI/CD pipeline configurations
│   └── ci_cd_pipeline.yml
└── README.md             # Documentation
```

## Prerequisites

- Python 3.9 or above
- Docker
- AWS CLI (for deployment)

## Setup and Usage

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application Locally
```bash
export SUPABASE_URL=<Your Supabase URL>
export SUPABASE_API_KEY=<Your Supabase API Key>
export CRED_URL=<Your Firebase Credentials URL>
python app.py
```

The application will be available at `http://localhost:8000`.

### 4. Build and Run with Docker
```bash
docker build -t canonical-interview .
docker run -d -p 8000:8000 --name canonical-container \
  -e SUPABASE_URL=<Your Supabase URL> \
  -e SUPABASE_API_KEY=<Your Supabase API Key> \
  -e CRED_URL=<Your Firebase Credentials URL> \
  canonical-interview
```

### 5. CI/CD Pipeline
The GitHub Actions pipeline automatically:
- Tests the application.
- Builds the Docker image.
- Deploys to an AWS EC2 instance.

To use the pipeline:
1. Add the following secrets in your repository:
   - `AWS_ACCESS_KEY_ID`
   - `AWS_SECRET_ACCESS_KEY`
   - `SUPABASE_URL`
   - `SUPABASE_API_KEY`
   - `CRED_URL`
   - `EC2_PUBLIC_IP`
   - `EC2_KEY`
2. Push your changes to the repository.

## API Endpoints

- **GET /**: Welcome message to verify the app is running.
- **GET /questions/nontechnicaltechnical**: Fetch non-technical questions from Supabase.
- **GET /questions/technical**: Fetch technical questions from Firebase.

## Deployment

The CI/CD pipeline automates deployment to AWS EC2. The Docker container is configured to restart and reflect updates with minimal downtime.

## Technology Stack

- **Backend**: Flask
- **Database**: Supabase, Firebase Firestore
- **Cloud**: AWS EC2
- **Containerization**: Docker
- **CI/CD**: GitHub Actions

## Security

- Sensitive environment variables (e.g., API keys) are securely managed via GitHub Secrets.
- Firebase credentials are fetched dynamically for secure initialization.
