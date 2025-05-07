import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
data = pd.read_csv('Train.csv')

# Preprocessing: Encode categorical features
label_encoder = LabelEncoder()
data['Warehouse_block'] = label_encoder.fit_transform(data['Warehouse_block'])
data['Mode_of_Shipment'] = label_encoder.fit_transform(data['Mode_of_Shipment'])
data['Product_importance'] = label_encoder.fit_transform(data['Product_importance'])
data['Gender'] = label_encoder.fit_transform(data['Gender'])

# Features and target
X = data.drop(columns=['Reached.on.Time_Y.N'])
y = data['Reached.on.Time_Y.N']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

# Train a model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'model.pkl')

# Evaluate the model
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
