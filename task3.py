# -*- coding: utf-8 -*-
"""TASK3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vdcJ4QwmzBVoXpgppSIUZ3e4F-c_fYLG

# **TASK3 IRIS FLOWER CLASSIFICATION**

Step1) Import the Libraries
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

"""Step2) Load the dataset"""

df = pd.read_csv('/content/IRIS.csv')

"""Step3) Import the Library to perform LinearRegression"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

"""Step4) Visualize the dataset"""

# Taking only the selected two attributes from the dataset
df.head()

df.info()

"""Step5) Split the data into features (X) and target variable (y)"""

X = df.drop('species', axis=1)
y = df['species']

"""Step6) Split the data into training and testing sets

"""

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

"""Step7) Standardize the features by scaling"""

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

"""As the attributes of the dataset are already numeric and data contains no null value lets perform classification

Step8) using DecisionTreeClassifier
"""

from sklearn.tree import DecisionTreeClassifier
# Create a Decision Tree classifier
dt_classifier = DecisionTreeClassifier(random_state=42)
# Train the classifier
dt_classifier.fit(X_train_scaled, y_train)
# Make predictions on the test set
y_pred_dt = dt_classifier.predict(X_test_scaled)
# Evaluate the model
accuracy_dt = accuracy_score(y_test, y_pred_dt)
print(f'Decision Tree Accuracy: {accuracy_dt:.2f}')

"""Step9) Classification using Logistic Regression"""

from sklearn.linear_model import LogisticRegression
# Create a Logistic Regression classifier
lr_classifier = LogisticRegression(random_state=42)
# Train the classifier
lr_classifier.fit(X_train_scaled, y_train)
# Make predictions on the test set
y_pred_lr = lr_classifier.predict(X_test_scaled)
# Evaluate the model
accuracy_lr = accuracy_score(y_test, y_pred_lr)
print(f'Logistic Regression Accuracy: {accuracy_lr:.2f}')