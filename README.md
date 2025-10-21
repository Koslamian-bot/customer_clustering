# 🤓 Mall Customer Segmentation using K-Means Clustering

## 📘 Project Overview

This project applies **K-Means Clustering** to group mall customers based on their **Annual Income** and **Spending Score**.
It helps businesses identify unique customer segments for better marketing strategies and personalized service.

---

## 🗁️ Repository Structure

```
📦 Project Root
 ┣ 🗂️ .ipynb_checkpoints
 ┣ 🗂️ venv
 ┣ 🖜 kmeans clustering.ipynb      ← Jupyter Notebook (training & visualization)
 ┣ 🖜 kmeans_model.joblib          ← Trained K-Means model
 ┣ 🖜 Mall_Customers.csv           ← Dataset used
 ┣ 🖜 predict_cluster.py           ← Script to predict which cluster a new customer belongs to
 ┗ 🖜 README.md                    ← Project documentation
```

---

## 🧩 Features

* Visualizes customer distribution and spending patterns.
* Finds optimal number of clusters using **Elbow Method**.
* Trains a **K-Means model** on income and spending score.
* Saves trained model as a `.joblib` file.
* Predicts cluster for any new customer input using a standalone script.

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-link>
cd <your-repo-folder>
```

### 2️⃣ Create a Virtual Environment (Optional)

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install pandas matplotlib scikit-learn joblib
```

---

## 🚀 Usage

### 🧮 1. Train and Visualize the Model

Open the notebook:

```bash
jupyter notebook "kmeans clustering.ipynb"
```

Run all cells to:

* Load the dataset
* Perform clustering
* Visualize clusters
* Save the trained model as `kmeans_model.joblib`

### 🔍 2. Predict Customer Cluster

After model training, run:

```bash
python predict_cluster.py
```

You’ll be prompted to enter:

```
Enter Annual Income (k$): 75
Enter Spending Score (1-100): 60
```

Then it will display:

```
🧭 The customer belongs to Cluster: 3
```

---

## 📊 Dataset Information

**File:** `Mall_Customers.csv`

| Column Name            | Description                                           |
| ---------------------- | ----------------------------------------------------- |
| CustomerID             | Unique ID for each customer                           |
| Gender                 | Male/Female                                           |
| Age                    | Age of the customer                                   |
| Annual Income (k$)     | Annual income in thousands                            |
| Spending Score (1-100) | Score assigned by the mall based on customer behavior |

---

## 🤓 Understanding Clusters (Example)

| Cluster | Characteristics                   |
| ------- | --------------------------------- |
| 0       | Low income, low spending          |
| 1       | High income, low spending         |
| 2       | Average income, moderate spending |
| 3       | High income, high spending        |
| 4       | Low income, high spending         |

*(Exact behavior may vary depending on random initialization.)*

---

## 📊 Future Enhancements

* Add GUI or web interface for predictions
* Extend clustering to include `Age` and `Gender`
* Compare with DBSCAN or Hierarchical clustering
* Add interactive dashboard visualizations (Plotly, Streamlit)

---

## 👨‍💻 Author

**Ravi Raahul aka ROWIN**

---

## 🖩️ License

This project is for educational purposes only. Feel free to modify and experiment with the code for your own learning.

---

## 💬 Acknowledgments

* Dataset Source: [Kaggle – Mall Customer Segmentation Data](https://www.kaggle.com/vjchoudhary7/customer-segmentation-tutorial-in-python)
* Inspired by real-world retail analytics use cases.
