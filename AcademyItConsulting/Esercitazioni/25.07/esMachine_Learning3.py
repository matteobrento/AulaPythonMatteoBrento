"""
Partendo dal dataset a questo link https://www.kaggle.com/datasets/nikhil7280/student-performance-multiple-linear-regression , 
utilizzate i dati sulle ore di studio e le ore di sonno per prevedere quanto queste caratteristiche influiscono sull'indice 
di prestazione degli studenti.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import PredictionErrorDisplay

df = pd.read_csv("C:\\Users\\matte\\AcademyItConsulting\\Esercitazioni\\25.07\\Student_Performance.csv")
print("Dataset Iniziale: \n", df, "\n")

X = df[['Hours Studied', 'Sleep Hours']]
y = df['Performance Index']

#X, y = np.array(X), np.array(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

regr = LinearRegression()
regr.fit(X, y)
predizione = regr.predict(X_test)
score = regr.score(X_train, y_train)
print("Score: ", score, "\n")
print("Performance Predette: \n",predizione, "\n")
print("Coefficiente: ", regr.coef_, "\n")
print("Intercetta: ", regr.intercept_, "\n")

display = PredictionErrorDisplay(y_true=y_test, y_pred=predizione)
display.plot()
plt.show()







