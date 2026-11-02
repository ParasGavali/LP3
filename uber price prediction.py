
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
df = pd.read_csv("uber.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())

# Convert date
df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])

# Create pickup hour
df['pickup_hour'] = df['pickup_datetime'].dt.hour

# Remove missing values
df.dropna(inplace=True)

# Remove fare outliers
Q1 = df['fare_amount'].quantile(0.01)
Q3 = df['fare_amount'].quantile(0.99)
df = df[(df['fare_amount'] > Q1) & (df['fare_amount'] < Q3)]

# Features and target
X = df[['pickup_longitude', 'pickup_latitude',
        'dropoff_longitude', 'dropoff_latitude',
        'passenger_count', 'pickup_hour']]
Y = df['fare_amount']

# Split data
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=1
)

# Linear Regression
lr = LinearRegression()
lr.fit(X_train, Y_train)
pred1 = lr.predict(X_test)

print("Linear Regression RMSE:",
      np.sqrt(mean_squared_error(Y_test, pred1)))
print("Linear Regression R2:", r2_score(Y_test, pred1))

# Random Forest
rf = RandomForestRegressor(n_estimators=100, random_state=101)
rf.fit(X_train, Y_train)
pred2 = rf.predict(X_test)

print("Random Forest RMSE:",
      np.sqrt(mean_squared_error(Y_test, pred2)))
print("Random Forest R2:", r2_score(Y_test, pred2))

# Fare boxplot
plt.boxplot(df['fare_amount'])
plt.title("Uber Fare Outliers")
plt.show()
