# Segmentación de clientes con clustering no supervisado: K-Means y DBSCAN
## 🇪🇸 Español

### Descripción del proyecto

Este proyecto aborda un problema de aprendizaje no supervisado aplicado a la segmentación de clientes, con el objetivo de identificar grupos homogéneos de clientes en función de su comportamiento de compra y características demográficas.

Se han aplicado dos algoritmos de clustering:

* K-Means, basado en centroides, para obtener una segmentación estructurada.
* DBSCAN, basado en densidad, para detectar clusters irregulares y posibles outliers.

Todo el flujo de trabajo se ha implementado mediante pipelines de scikit-learn, garantizando un proceso modular, reproducible y escalable.

### Objetivo
* Identificar patrones ocultos en el comportamiento de los clientes
* Segmentar clientes en grupos homogéneos
* Comparar diferentes enfoques de clustering
* Extraer insights accionables para negocio

### 📁 Dataset

El dataset contiene información de clientes de un centro comercial:

* ID de cliente
* Género
* Edad
* Ingreso anual (k$)
* Score de gasto (1–100)

No existen valores nulos, lo que facilita el análisis directo mediante técnicas de clustering.

### Metodología
#### 🔎 Análisis exploratorio (EDA)

Distribución de variables
Relaciones entre ingresos, edad y gasto
Visualización de patrones en los datos

#### 🧼 Preprocesamiento
Escalado de variables numéricas
Codificación de variables categóricas cuando aplica
Estructuración mediante pipelines

#### 🤖 Modelos de clustering
##### K-Means
Selección del número óptimo de clusters
Evaluación mediante silhouette score
Segmentación estable y equilibrada

##### DBSCAN
Ajuste de hiperparámetros (eps, min_samples)
Identificación de clusters basados en densidad
Detección de outliers

### 📊 Resultados principales
#### K-Means
Segmentación clara y estructurada
Todos los clientes son asignados a un cluster
Alta interpretabilidad para negocio

#### DBSCAN
5 clusters identificados
Aproximadamente 17% de outliers
Detección de comportamientos atípicos

### 🧩 Insights de negocio

Se identifican los siguientes perfiles de clientes:

* Clientes de alto valor: ingresos y gasto elevados → prioridad estratégica
* Clientes potenciales: altos ingresos pero bajo gasto → oportunidad de crecimiento
* Clientes de bajo valor: bajo ingreso y bajo gasto → baja prioridad
* Clientes intermedios: comportamiento equilibrado
* Outliers: comportamientos no estándar detectados por DBSCAN

### 📌 Conclusiones
K-Means es adecuado para segmentación operativa clara y estable
DBSCAN complementa el análisis detectando ruido y estructuras complejas
La combinación de ambos modelos proporciona una visión más completa del cliente

### 🛠️ Tecnologías
Python
Pandas / NumPy
Scikit-learn
Matplotlib / Seaborn
Pipelines de ML

### Ejecución
pip install -r requirements.txt
jupyter notebook

### 📁 Estructura del repositorio

```
customer-segmentation/
│
├── main.py
├── pipeline.py
├── README.md                            
│
└── data/
    ├── Mall_Customers.csv
└── models/
    ├── dbscan.pkl
    ├── kmeans.pkl
└── notebooks/
    ├── customer-segmentation-clustering.ipynb
```

## 🚀 Despliegue de la API 

Se ha desarrollado una API REST utilizando **FastAPI** para servir el modelo de clustering K-Means en producción.

La API está desplegada en Render y permite realizar predicciones en tiempo real para la segmentación de clientes.

### 🌐 URL base
URL API: [https://ml-customer-segmentation-1.onrender.com]


#### Endpoint principal

**Predicción de cliente**
```

POST /predict

```

**Ejemplo de entrada:**

```json id="in1"
{
  "age": 30,
  "income": 70,
  "spending_score": 40
}
```

**Salida:**

```json id="out1"
{
  "cluster": 2
}
```
### Autora
| Rebeca Prior | [@rebecaprg](https://github.com/rebecaprg) |

---


# Customer segmentation with unsupervised clustering: K-Means and DBSCAN
## 🇬🇧 English

### Project description

This project addresses an unsupervised learning problem applied to customer segmentation, with the aim of identifying homogeneous groups of customers based on their purchasing behavior and demographic characteristics.

Two clustering algorithms have been applied:

* K-Means, based on centroids, to obtain a structured segmentation.
* DBSCAN, based on density, to detect irregular clusters and possible outliers.

The entire workflow has been implemented using scikit-learn pipelines, ensuring a modular, reproducible, and scalable process.

### Objective
* Identify hidden patterns in customer behavior
* Segment customers into homogeneous groups
* Compare different clustering approaches
* Extract actionable business insights

### 📁 Dataset

The dataset contains information about customers of a shopping mall:

* Customer ID
* Gender
* Age
* Annual income (k$)
* Spending score (1–100)

There are no missing values, which facilitates direct analysis using clustering techniques.

### Methodology

#### 🔎 Exploratory Data Analysis (EDA)

Distribution of variables
Relationships between income, age and spending
Visualization of patterns in the data

#### 🧼 Preprocessing

Scaling of numerical variables
Encoding of categorical variables when applicable
Structuring using pipelines

#### 🤖 Clustering models
##### K-Means

Selection of optimal number of clusters
Evaluation using silhouette score
Stable and balanced segmentation

##### DBSCAN

Hyperparameter tuning (eps, min_samples)
Identification of density-based clusters
Detection of outliers

### 📊 Main results
##### K-Means

Clear and structured segmentation
All customers are assigned to a cluster
High interpretability for business use

##### DBSCAN

5 clusters identified
Approximately 17% of outliers
Detection of atypical behavior

### 🧩 Business insights

The following customer profiles are identified:

* High-value customers: high income and high spending → strategic priority
* Potential customers: high income but low spending → growth opportunity
* Low-value customers: low income and low spending → low priority
* Intermediate customers: balanced behavior
* Outliers: non-standard behaviors detected by DBSCAN

### 📌 Conclusions

* K-Means is suitable for clear and stable operational segmentation
* DBSCAN complements the analysis by detecting noise and complex structures
* The combination of both models provides a more complete view of the customer

### 🛠️ Technologies

Python
Pandas / NumPy
Scikit-learn
Matplotlib / Seaborn
ML Pipelines

### Execution

pip install -r requirements.txt
jupyter notebook

### 📁 Repository structure
```
customer-segmentation/
│
├── main.py
├── pipeline.py
├── README.md                            
│
└── data/
    ├── Mall_Customers.csv
└── models/
    ├── dbscan.pkl
    ├── kmeans.pkl
└── notebooks/
    ├── customer-segmentation-clustering.ipynb
```
### 🚀 API Deployment

A REST API has been developed using **FastAPI** to serve the K-Means clustering model in production.

The API is deployed on Render and enables real-time predictions for customer segmentation.

### 🌐 Base URL
API URL: [https://ml-customer-segmentation-1.onrender.com]

---

#### Main endpoint

**Customer prediction**

POST /predict


**Input example:**

```json
{
  "age": 30,
  "income": 70,
  "spending_score": 40
}
```
Output:
```
{
  "cluster": 2
}
```
### Authora

| Rebeca Prior | [@rebecaprg](https://github.com/rebecaprg) |
