
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load dataset
df = pd.read_csv("emails.csv")

print(df.head())
print(df.isnull().sum())

# Features and target
X = df.iloc[:, 1:3001]
Y = df.iloc[:, -1]

# Outlier detection
Q1 = X.quantile(0.25)
Q3 = X.quantile(0.75)
IQR = Q3 - Q1

outliers = ((X < Q1 - 1.5*IQR) | (X > Q3 + 1.5*IQR)).sum()
top = outliers.nlargest(12).index

sns.boxplot(data=X[top])
plt.xticks(rotation=45)
plt.show()

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.25, random_state=42
)

# SVM
svm = SVC(kernel='rbf')
svm.fit(X_train, y_train)
pred = svm.predict(X_test)

print("\nSVM Accuracy:", accuracy_score(y_test, pred))
print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred))

# KNN
knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(X_train, y_train)
pred = knn.predict(X_test)

print("\nKNN Accuracy:", accuracy_score(y_test, pred))
print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred))

# Feature Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Compare different K values
for k in [1, 3, 5]:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    pred = knn.predict(X_test)

    print("\nK =", k)
    print("Accuracy:", accuracy_score(y_test, pred))
    print(confusion_matrix(y_test, pred))
    print(classification_report(y_test, pred, zero_division=0))
