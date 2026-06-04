import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

# FastAPI App initialize karein
app = FastAPI(title="Real-Time Fraud Detection API", version="1.0")

# Trained model ko load karein jo train.py se bana tha
try:
    model = joblib.load("model.pkl")
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")

# User input ka structure (Schema) define karein
# Credit card dataset mein 30 features hain: Time, V1-V28, aur Amount
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
    return {"message": "Fraud Detection API is Running Live!"}

@app.post("/predict")
def predict_fraud(data: TransactionData):
    # Input data ko dictionary se list/array mein convert karein
    input_features = [
        data.Time, data.V1, data.V2, data.V3, data.V4, data.V5,
        data.V6, data.V7, data.V8, data.V9, data.V10, data.V11,
        data.V12, data.V13, data.V14, data.V15, data.V16, data.V17,
        data.V18, data.V19, data.V20, data.V21, data.V22, data.V23,
        data.V24, data.V25, data.V26, data.V27, data.V28, data.Amount
    ]
    
    # Model se prediction lein
    prediction = model.predict([input_features])[0]
    
    # Agar output 1 hai to Fraud, agar 0 hai to Legitimate
    status = "Fraudulent" if prediction == 1 else "Legitimate"
    
    return {
        "prediction_code": int(prediction),
        "status": status
    }

# Windows Terminal automatic shutdown ko bypass karne ke liye direct execution block
if __name__ == "__main__":
    import uvicorn
    print("Starting FastAPI Server via Python Script...")
    uvicorn.run(app, host="127.0.0.1", port=8000)