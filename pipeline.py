from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.cluster import DBSCAN

#Base
num_cols = ["Age", "Annual Income (k$)", "Spending Score (1-100)"]

base_pipeline = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), num_cols)
    ]
)

#KMEANS

def build_kmeans_pipeline(n_clusters):

    return Pipeline(steps=[
        ("preprocessing", base_pipeline),
        ("model", KMeans(n_clusters=n_clusters, random_state=42))
    ])

best_k = 6

kmeans_pipeline = build_kmeans_pipeline(best_k)

kmeans_pipeline.fit(df)

labels_kmeans = kmeans_pipeline.named_steps["model"].labels_

df_clusters = df.copy()
df_clusters["cluster"] = labels_kmeans

print(df_clusters.groupby("cluster")[num_cols].mean())


X_final = kmeans_pipeline[:-1].transform(df)
sil_score = silhouette_score(X_final, labels_kmeans)

print("Silhouette:", sil_score)


#DBSCAN


def build_dbscan_pipeline(eps, min_samples):

    return Pipeline(steps=[
        ("preprocessing", base_pipeline),
        ("model", DBSCAN(eps=eps, min_samples=min_samples))
    ])

final_dbscan_pipeline = build_dbscan_pipeline(
    eps=0.6,
    min_samples=6
)

final_dbscan_pipeline.fit(df)

labels_dbscan = final_dbscan_pipeline.named_steps["model"].labels_

n_clusters = len(set(labels_dbscan)) - (1 if -1 in labels_dbscan else 0)
outliers = np.sum(labels_dbscan == -1)

print("Clusters detectados:", n_clusters)
print("Outliers:", outliers)
print("Porcentaje:", 100 * outliers / len(labels_dbscan))

df_dbscan = df.copy()
df_dbscan["cluster"] = labels_dbscan

df_dbscan[df_dbscan["cluster"] != -1].groupby("cluster")[num_cols].mean()