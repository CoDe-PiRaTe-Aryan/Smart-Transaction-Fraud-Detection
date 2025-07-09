# train_model.py

import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

print("📥 Loading dataset...")
# ✅ Correct relative path from backend folder
df = pd.read_csv("../data/PaySim_sample.csv")

# ✅ Filter only TRANSFER and CASH_OUT (since most frauds are in these)
df = df[df['type'].isin(['TRANSFER', 'CASH_OUT'])]

# ✅ Encode 'type' as binary: TRANSFER=0, CASH_OUT=1
df['type'] = df['type'].map({'TRANSFER': 0, 'CASH_OUT': 1})

# ✅ Select only 5 realistic features
selected_features = ['amount', 'oldbalanceOrg', 'newbalanceOrig', 'type', 'isFlaggedFraud']
X = df[selected_features]
y = df['isFraud']

# ✅ Feature Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ✅ Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# ✅ Train Model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ✅ Save model and scaler inside backend folder
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

print("✅ Model trained on 5 realistic features and saved!")
