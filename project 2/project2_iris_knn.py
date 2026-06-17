import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, f1_score

# =====================================================================
# PHASE 1: INPUT & DATA HANDLING
# =====================================================================
iris = load_iris()
X = iris.data
y = iris.target

# =====================================================================
# PHASE 2: PROCESSING (The Algorithmic Pipeline)
# =====================================================================

# ADJUSTED: Added stratify=y and set test_size=0.3 per kit parameters
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,       # Meets standard training kit distribution baseline
    random_state=42,     # Ensures reproducible shuffle behavior
    stratify=y           # Mandatory for structural class balancing
)

# Feature scaling (StandardScaler: Mean=0, Variance=1)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# KNN model instantiation (k=5 neighbors)
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

# =====================================================================
# PHASE 3: OUTPUT & VALIDATION
# =====================================================================
y_pred = model.predict(X_test)

print("========================================================")
print("             DECODELABS PROJECT 2 METRICS               ")
print("========================================================")
print("Accuracy:", accuracy_score(y_test, y_pred))

# Added explicit F1-Score metric highlighting as requested by page 7 blueprint
print("Macro F1-Score:", f1_score(y_test, y_pred, average='macro'))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))
print("========================================================")