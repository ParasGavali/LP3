
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load dataset
data = pd.read_csv("diabetes.csv")

print(data.head())
print(data.isnull().sum())

# Replace zero values with mean
cols = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']

for col in cols:
    data[col] = data[col].replace(0, np.nan)
    data[col] = data[col].fillna(data[col].mean())

# Features and target
X = data.drop('Outcome', axis=1)
Y = data['Outcome']

# Split data
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=0, stratify=Y
)

# Feature scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Outlier detection
sns.boxplot(data=data.drop('Outcome', axis=1))
plt.xticks(rotation=45)
plt.show()

Q1 = X_train.shape[1]  # Number of features
Q1 = data.drop('Outcome', axis=1).quantile(0.25)
Q3 = data.drop('Outcome', axis=1).quantile(0.75)
IQR = Q3 - Q1

outliers = ((data.drop('Outcome', axis=1) < Q1 - 1.5*IQR) |
            (data.drop('Outcome', axis=1) > Q3 + 1.5*IQR)).sum()

print("Outliers:\n", outliers)

# KNN model
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, Y_train)
pred = knn.predict(X_test)

# Evaluation
cm = confusion_matrix(Y_test, pred)
acc = accuracy_score(Y_test, pred)

print("\nConfusion Matrix:\n", cm)
print("Accuracy:", acc)
print("Error Rate:", 1-acc)
print("Classification Report:\n", classification_report(Y_test, pred, zero_division=0))

# Compare K values
scores = []

for k in [3, 5, 7]:
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, Y_train)
    scores.append(accuracy_score(Y_test, model.predict(X_test)))

print("KNN Accuracy:", scores)

# Accuracy graph
plt.plot([3, 5, 7], scores, marker='o')
plt.xlabel("K Value")
plt.ylabel("Accuracy")
plt.title("KNN Accuracy Comparison")
plt.grid()
plt.show()

# Confusion matrix graph
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()

print("Diabetes Prediction Completed!")
