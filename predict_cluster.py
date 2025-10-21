# predict_cluster.py

import joblib
import pandas as pd
from sklearn.cluster import KMeans
import os

MODEL_PATH = "kmeans_model.joblib"

def train_and_save_model():
    """Train the model if no saved model is found."""
    print("Training KMeans model (first-time setup)...")
    df = pd.read_csv("Mall_Customers.csv")
    X = df[['Annual Income (k$)', 'Spending Score (1-100)']]
    
    model = KMeans(n_clusters=5, random_state=42)
    model.fit(X)
    
    joblib.dump(model, MODEL_PATH)
    print("Model trained and saved as:", MODEL_PATH)
    return model

def load_model():
    """Load model if exists, else train it."""
    if os.path.exists(MODEL_PATH):
        print("Loading existing KMeans model...")
        return joblib.load(MODEL_PATH)
    else:
        return train_and_save_model()

def predict_cluster(annual_income, spending_score):
    """Predict which cluster a customer falls into."""
    model = load_model()
    data = pd.DataFrame([[annual_income, spending_score]],
                        columns=['Annual Income (k$)', 'Spending Score (1-100)'])
    cluster = model.predict(data)[0]
    print(f"\n🧭 The customer belongs to Cluster: {cluster}")

if __name__ == "__main__":
    print("=== Customer Cluster Prediction ===")
    income = float(input("Enter Annual Income (k$): "))
    score = float(input("Enter Spending Score (1-100): "))
    predict_cluster(income, score)


#20 - 20 -->cluster 2
#70 - 90 --> cluster 4
#90 - 10 --> cluster 1

# mostly the customers will be on cluster 3