curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'Content-Type: application/json' \
  -d '{
      "Warehouse_block": "A",
      "Mode_of_Shipment": "Ship",
      "Customer_care_calls": 0,
      "Customer_rating": 4,
      "Cost_of_the_Product": 100.5,
      "Prior_purchases": 2,
      "Product_importance": "medium",
      "Gender": "Male",
      "Discount_offered": 10,
      "Weight_in_gms": 1500
 }'
