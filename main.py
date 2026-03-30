from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import pickle
#load the model
with open("xgb_model.pkl","rb") as f:
    model = pickle.load(f)
app = FastAPI()

#define
class ItemData(BaseModel):
     Category: int
     Item: int
     Price_Per_Unit: float
     Quantity: float
     Discount_Applied: int
     Payment_Method_Cash: int
     Payment_Method_Credit_Card: int
     Payment_Method_Digital_Wallet: int
     Location_In_store: int
     Location_Online: int
@app.get("/")
def read_root():
     return{"message":"API is working"}
@app.post("/predict")
def predict_total_spent(data: ItemData):
    input_df = pd.DataFrame([data.dict()])
    prediction = model.predict(input_df)
    return {"predicted_total_spent": float(prediction[0])}