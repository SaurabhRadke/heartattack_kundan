# create_models.py
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

os.makedirs('models', exist_ok=True)

# Load and prepare data
df = pd.read_csv('heart.csv')
feature_cols = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 
                'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
X = df[feature_cols]
y = df['target']

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_scaled = pd.DataFrame(X_scaled, columns=feature_cols)

# Train and save
model = RandomForestClassifier(random_state=42)
model.fit(X_scaled, y)

joblib.dump(scaler, 'models/scaler.pkl')
joblib.dump(model, 'models/best_randomforest_model.pkl')