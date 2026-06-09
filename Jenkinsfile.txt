pipeline {
    agent any

    environment {
        REGISTRY = "ahadali123/fraud-detection-mlops"
        IMAGE_TAG = "${BUILD_NUMBER}"
        MLFLOW_TRACKING_URI = "http://localhost:5000"
    }

    stages {
        stage('Checkout Source Code') {
            steps {
                echo 'Pulling latest code from GitHub Repository...'
                checkout scm
            }
        }

        stage('Environment & Dependencies Setup') {
            steps {
                echo 'Installing required Python libraries...'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Model Training & MLflow Tracking') {
            steps {
                echo 'Executing model training and logging metrics to MLflow Tracking Server...'
                sh 'python train.py'
            }
        }

        stage('Docker Image Build') {
            steps {
                echo 'Building production Docker image for Fraud Detection Model...'
                sh "docker build -t ${REGISTRY}:${IMAGE_TAG} ."
                sh "docker build -t ${REGISTRY}:latest ."
            }
        }

        stage('Automated Production Deployment') {
            steps {
                echo 'Deploying model container using Kubernetes Manifests...'
                sh "kubectl apply -f kubernetes/deployment.yaml"
                sh "kubectl apply -f kubernetes/service.yaml"
                echo 'MLOps Continuous Deployment (CD) Pipeline Completed Successfully!'
            }
        }
    }

    post {
        success {
            echo 'Pipeline Passed Successfully! Model is live.'
        }
        failure {
            echo 'Pipeline Failed! Check logs for debugging.'
        }
    }
}