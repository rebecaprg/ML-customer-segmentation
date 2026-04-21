from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pandas as pd
from pathlib import Path
import joblib

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "kmeans.pkl"

kmeans_pipeline = joblib.load(MODEL_PATH)

app = FastAPI(title="Customer Segmentation API")


class Customer(BaseModel):
    age: float
    income: float
    spending_score: float


def preprocess(data: Customer):
    return pd.DataFrame([{
        "Age": data.age,
        "Annual Income (k$)": data.income,
        "Spending Score (1-100)": data.spending_score
    }])


@app.get("/")
def home():
    return {"message": "API running 🚀"}




@app.post("/predict")
def predict(customer: Customer):
    X = preprocess(customer)
    cluster = int(kmeans_pipeline.predict(X)[0])
    return {"cluster": cluster}