from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
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
    return np.array([[data.age, data.income, data.spending_score]])


@app.get("/")
def home():
    return {"message": "API running 🚀"}

@app.get("/debug-model")
def debug_model():
    return {"model_type": str(type(kmeans_pipeline))}


@app.post("/predict")
def predict(customer: Customer):
    X = preprocess(customer)
    cluster = int(kmeans_pipeline.predict(X)[0])
    return {"cluster": cluster}