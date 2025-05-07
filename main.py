from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib
import os

app = FastAPI()

# Ensure the model is loaded from the correct path
model_path = "model.pkl"
if not os.path.exists(model_path):
    raise FileNotFoundError(f"{model_path} not found")

model = joblib.load(model_path)

# Simple label encodings (must match training)
warehouse_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'F': 4}
mode_map = {'Ship': 0, 'Flight': 1, 'Road': 2}
importance_map = {'low': 0, 'medium': 1, 'high': 2}
gender_map = {'Male': 0, 'Female': 1}

# Pydantic model for request body
class ShipmentRequest(BaseModel):
    Warehouse_block: str
    Mode_of_Shipment: str
    Customer_care_calls: int
    Customer_rating: int
    Cost_of_the_Product: float
    Prior_purchases: int
    Product_importance: str
    Gender: str
    Discount_offered: float
    Weight_in_gms: float

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Shipment Prediction API"}

# Prediction endpoint
@app.post("/predict")
def predict_shipment(arrival: ShipmentRequest):
    try:
        # Encode categorical variables
        warehouse = warehouse_map.get(arrival.Warehouse_block, -1)
        mode = mode_map.get(arrival.Mode_of_Shipment, -1)
        importance = importance_map.get(arrival.Product_importance, -1)
        gender = gender_map.get(arrival.Gender, -1)

        # Feature array with 11 inputs (after encoding)
        features = np.array([
            warehouse,
            mode,
            arrival.Customer_care_calls,
            arrival.Customer_rating,
            arrival.Cost_of_the_Product,
            arrival.Prior_purchases,
            importance,
            gender,
            arrival.Discount_offered,
            arrival.Weight_in_gms,
            0  # Placeholder for extra features if needed
        ]).reshape(1, -1)

        prediction = model.predict(features)[0]
        return {"prediction": int(prediction)}

    except Exception as e:
        return {"error": str(e)}
