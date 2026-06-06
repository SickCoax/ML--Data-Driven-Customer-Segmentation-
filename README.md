# Customer Segmentation using K-Means Clustering

## Overview

This project performs customer segmentation on an e-commerce retail dataset using K-Means Clustering. The objective is to identify customer groups based on purchasing behavior and generate business insights.

---

## Dataset

**Online Retail Dataset**

The dataset contains transactional information such as:

- CustomerID
- InvoiceNo
- StockCode
- Quantity
- UnitPrice
- InvoiceDate

---

## Data Preprocessing

- Removed missing Customer IDs
- Removed cancelled/returned transactions (`Quantity <= 0`)
- Created `TotalPrice` feature
- Aggregated transaction data at customer level
- Standardized features using `StandardScaler`

---

## Feature Engineering

The following customer-level features were created:

- Total Spending (`TotalPrice_sum`)
- Maximum Purchase Value (`TotalPrice_max`)
- Total Items Purchased (`Quantity_sum`)
- Distinct Products Purchased (`Distinct_Product`)
- Purchase Frequency (`Frequency`)

---

## Model

**K-Means Clustering**

Cluster selection was performed using:

- Elbow Method
- Silhouette Score

---

## Visualization

Principal Component Analysis (PCA) was used to reduce dimensions and visualize customer clusters.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-Learn

---

## Project Workflow

```text
Raw Data
    ↓
Data Cleaning
    ↓
Feature Engineering
    ↓
Feature Scaling
    ↓
K-Means Clustering
    ↓
Cluster Evaluation
    ↓
PCA Visualization
```

## Results

The model successfully segmented customers into distinct groups based on purchasing patterns, enabling better customer understanding and targeted business strategies.