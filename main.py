import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans, DBSCAN
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import joblib

#Cargar datos
df = pd.read_csv("data/Mall_Customers.csv")

num_cols = ["Age", "Annual Income (k$)", "Spending Score (1-100)"]

#Base pipeline
base_pipeline = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), num_cols)
    ]
)


# 3. KMEANS
kmeans_pipeline = Pipeline(steps=[
    ("preprocessing", base_pipeline),
    ("model", KMeans(n_clusters=6, random_state=42))
])

kmeans_pipeline.fit(df)

labels_kmeans = kmeans_pipeline.named_steps["model"].labels_

df["kmeans_cluster"] = labels_kmeans

print("\nKMEANS RESULTS")
print(df.groupby("kmeans_cluster")[num_cols].mean())

X_kmeans = kmeans_pipeline[:-1].transform(df)
print("Silhouette KMeans:", silhouette_score(X_kmeans, labels_kmeans))



# 4. DBSCAN
dbscan_pipeline = Pipeline(steps=[
    ("preprocessing", base_pipeline),
    ("model", DBSCAN(eps=0.6, min_samples=6))
])

dbscan_pipeline.fit(df)

labels_dbscan = dbscan_pipeline.named_steps["model"].labels_

df["dbscan_cluster"] = labels_dbscan

print("\nDBSCAN RESULTS")
print("Clusters:", len(set(labels_dbscan)) - (1 if -1 in labels_dbscan else 0))
print("Outliers:", sum(labels_dbscan == -1))

print(
    df[df["dbscan_cluster"] != -1]
    .groupby("dbscan_cluster")[num_cols]
    .mean()
)


print("Guardando modelo KMeans...")

joblib.dump(kmeans_pipeline, "models/kmeans.pkl")
joblib.dump(dbscan_pipeline, "models/dbscan.pkl")

print("KMeans guardado")

