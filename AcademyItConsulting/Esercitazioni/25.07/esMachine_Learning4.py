"""
Partendo dal dataset a questo link https://www.kaggle.com/datasets/quantbruce/real-estate-price-prediction , 
utilizzate i dati sugli anni delle case e la distanza dalla stazione metro per prevedere quanto queste caratteristiche 
influiscono sul costo delle case.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import PredictionErrorDisplay

df = pd.read_csv("C:\\Users\\matte\\AcademyItConsulting\\Esercitazioni\\25.07\\Real estate.csv")
print("Dataset Iniziale: \n", df, "\n")

X = df[['X2 house age', 'X3 distance to the nearest MRT station']]
y = df['Y house price of unit area']

#X, y = np.array(X), np.array(y)

X_train, X_test, y_train, y_test = train_test_split(X, y)

regressione = LinearRegression()
regressione.fit(X,y)
predizione = regressione.predict(X_test)
score = regressione.score(X_train, y_train)
print("Score: ", score, "\n")
print("Performance Predette: \n",predizione, "\n")
print("Coefficiente: ", regressione.coef_, "\n")
print("Intercetta: ", regressione.intercept_, "\n")

plt.figure(figsize=(10,5))
plt.subplot(1,2,1).set_title("Relazione: House Age - House Price")
plt.scatter(X_test['X2 house age'], y_test, color="red")
plt.scatter(X_test['X2 house age'], predizione, color="blue")

plt.subplot(1,2,2).set_title("Relazione: Distance to Station - House Price")
plt.scatter(X_test['X3 distance to the nearest MRT station'], y_test, color="red")
plt.scatter(X_test['X3 distance to the nearest MRT station'], predizione, color="blue")
plt.show()

display = PredictionErrorDisplay(y_true=y_test, y_pred=predizione)
display.plot()
plt.show()