import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Real-Time Fraud Detection API (With Production Monitoring)", version="1.0")

# Prometheus Instrumentator auto /metrics endpoint banayega
Instrumentator().instrument(app).expose(app)

try:
    model = joblib.load("model.pkl")
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")

class TransactionData(BaseModel):
    Time: float
    V1: float; V2: float; V3: float; V4: float; V5: float
    V6: float; V7: float; V8: float; V9: float; V10: float
    V11: float; V12: float; V13: float; V14: float; V15: float
    V16: float; V17: float; V18: float; V19: float; V20: float
    V21: float; V22: float; V23: float; V24: float; V25: float
    V26: float; V27: float; V28: float
    Amount: float

@app.get("/")
def home():
    return {"message": "Fraud Detection API is Running Live with Prometheus Monitoring!"}

@app.post("/predict")
def predict_fraud(data: TransactionData):
    input_features = [
        data.Time, data.V1, data.V2, data.V3, data.V4, data.V5,
        data.V6, data.V7, data.V8, data.V9, data.V10, data.V11,
        data.V12, data.V13, data.V14, data.V15, data.V16, data.V17,
        data.V18, data.V19, data.V20, data.V21, data.V22, data.V23,
        data.V24, data.V25, data.V26, data.V27, data.V28, data.Amount
    ]
    prediction = model.predict([input_features])[0]
    status = "Fraudulent" if prediction == 1 else "Legitimate"
    return {"prediction_code": int(prediction), "status": status}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)