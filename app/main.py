from fastapi import FastAPI
import pandas as pd
import numpy as np
import joblib
from pydantic import BaseModel
import warnings
warnings.filterwarnings("ignore")

app = FastAPI()

model = joblib.load('C:/Users/bikas/Desktop/Fraud_detection/src/model.pkl')

expected_features = ['step', 'type', 'amount', 'nameOrig', 'oldbalanceOrg', 'newbalanceOrig', 'nameDest', 'oldbalanceDest', 'newbalanceDest', 'isFraud', 'isFlaggedFraud']

class TransactionData(BaseModel):
    step: int
    type: str  
    amount: float
    oldbalanceOrg: float
    newbalanceOrig: float
    oldbalanceDest: float
    newbalanceDest: float

# Root endpoint to check if API is working
@app.get("/")
def read_root():
    return {"Message": "API is working!!"}

# Prediction endpoint
@app.post("/predict/")
def predict_fraud(data: TransactionData):
    
    # Converting incoming data to a dictionary
    data_dict = data.dict()

    type_dummies = pd.get_dummies([data_dict['type']], prefix ='type')

    expected_columns = ['CASH_IN', 'CASH_OUT', 'DEBIT', 'PAYMENT', 'TRANSFER']
    for col in expected_columns:
        if col not in type_dummies.columns:
            type_dummies[col] = 0

    del data_dict['type']

    data_df = pd.DataFrame([data_dict])

    final_data = pd.concat([data_df, type_dummies[expected_columns]], axis = 1)

    for col in expected_features:
        if col not in final_data.columns:
            final_data[col] = 0

    final_data = final_data[expected_features]

    prediction = model.predict(final_data)

    return {"prediction": int(prediction[0])}