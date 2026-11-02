
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Load dataset
df = pd.read_csv("Churn_Modelling.csv")

print(df.head())
print(df.isnull().sum())

# Features and target
X = df.drop(columns=['Exited', 'RowNumber', 'CustomerId', 'Surname'])
y = df['Exited']

# Convert categorical data into numbers
X = pd.get_dummies(X, drop_first=True, dtype=int)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Feature scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Create Neural Network
model = MLPClassifier(
    hidden_layer_sizes=(6, 6),
    activation='relu',
    solver='adam',
    max_iter=20,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Training accuracy
train_acc = model.score(X_train, y_train)

# Predict test data
pred = model.predict(X_test)

# Evaluation
acc = accuracy_score(y_test, pred)
cm = confusion_matrix(y_test, pred)

print("\nTraining Accuracy:", train_acc * 100)
print("Testing Accuracy:", acc * 100)
print("\nConfusion Matrix:\n", cm)
print("\nClassification Report:\n", classification_report(y_test, pred, zero_division=0))

# Confusion matrix graph
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Customer Churn Prediction")
plt.show()

# Accuracy graph
plt.bar(['Training', 'Testing'], [train_acc*100, acc*100])
plt.ylabel("Accuracy (%)")
plt.title("Neural Network Accuracy")
plt.ylim(0, 100)
plt.show()

print("Program Executed Successfully!")
