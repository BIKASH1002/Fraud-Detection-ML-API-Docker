import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

df = pd.read_csv('C:/Users/bikas/Desktop/Fraud_detection/data/financial_fraud.csv')

df = pd.get_dummies(df, columns = ['type'], drop_first = True)
X = df.drop(['isFraud', 'nameOrig', 'nameDest'], axis = 1)
y = df['isFraud']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = RandomForestClassifier(n_estimators = 100, random_state = 42)
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100: .2f}%")

joblib.dump(model, 'C:/Users/bikas/Desktop/Fraud detection/src/model.pkl')
print("Model Dumped!!")
