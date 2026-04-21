from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os

# Cargar el modelo
kmeans_pipeline = joblib.load("models/kmeans.pkl")

kmeans_pipeline = joblib.load(MODEL_PATH)

app = FastAPI(title="Customer Segmentation API")


# Input
class Customer(BaseModel):
    age: float
    income: float
    spending_score: float


# Preprocess (input) 
def preprocess(data: Customer):

    return np.array([[
        data.age,
        data.income,
        data.spending_score
    ]])


# Interpretacion de clusters 
def interpret_cluster(cluster):

    mapping = {
        0: "Moderate Customers",
        1: "High Value Customers",
        2: "Young High Spenders",
        3: "Average Customers",
        4: "Low Spenders High Income",
        5: "Low Value Customers"
    }

    return mapping.get(cluster, "Unknown")


# Endpoints
@app.get("/")
def home():
    return {"message": "API running 🚀"}


@app.post("/predict")
def predict(customer: Customer):

    X = preprocess(customer)

    cluster = int(kmeans_pipeline.predict(X)[0])

    return {
        "cluster": cluster,
        "segment": interpret_cluster(cluster)
    }