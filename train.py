import os
# Windows space path error aur latest MLflow check ko bypass karne ki settings
os.environ['MLFLOW_TRACKING_URI'] = 'file:./tracking_data'
os.environ['MLFLOW_ALLOW_FILE_STORE'] = 'true'

import mlflow
import mlflow.sklearn
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

print("Loading real-world dataset...")
# Load the dataset from the same directory
df = pd.read_csv("creditcard.csv")

# Splitting features and target label (Class: 1 for Fraud, 0 for Legitimate)
X = df.drop(columns=['Class'])
y = df['Class']

print("Splitting data into train and test sets...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Initialize MLflow experiment
mlflow.set_experiment("Fraud_Detection_System")

print("Starting training inside MLflow experiment tracking...")
with mlflow.start_run():
    # Parameters
    n_estimators = 50
    max_depth = 8
    
    # Random Forest Model Setup
    model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)
    
    # Model evaluation
    predictions = model.predict(X_test)
    acc = accuracy_score(y_test, predictions)
    
    # Log parameters and metrics to MLflow dashboard
    mlflow.log_param("n_estimators", n_estimators)
    mlflow.log_param("max_depth", max_depth)
    mlflow.log_metric("accuracy", acc)
    
    # Save model binary locally for FastAPI usage
    joblib.dump(model, "model.pkl")
    
    # Log and register the model with MLflow Model Registry
    mlflow.sklearn.log_model(model, "fraud_model", registered_model_name="RandomForestFraudModel")
    
    print(f"--- Training Complete! ---")
    print(f"Model Accuracy: {acc * 100:.2f}%")
    print("Model saved locally as 'model.pkl' and tracked in MLflow registry.")