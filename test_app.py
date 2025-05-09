from fastapi.testclient import TestClient
from main import app, model
import numpy as np

client = TestClient(app)

# Unit test for model prediction
def test_model_prediction():
    features = np.array([[0, 0, 2, 4, 150.0, 2, 1, 0, 10, 1800, 0]])
    prediction = model.predict(features)
    assert prediction[0] in [0, 1]

# Integration test for API endpoint
def test_api_predict():
    response = client.post("/predict", json={
        "Warehouse_block": "A",
        "Mode_of_Shipment": "Ship",
        "Customer_care_calls": 2,
        "Customer_rating": 4,
        "Cost_of_the_Product": 150.0,
        "Prior_purchases": 2,
        "Product_importance": "medium",
        "Gender": "Male",
        "Discount_offered": 10,
        "Weight_in_gms": 1800
    })
    assert response.status_code == 200
    assert "prediction" in response.json()
    assert response.json()["prediction"] in [0, 1]
