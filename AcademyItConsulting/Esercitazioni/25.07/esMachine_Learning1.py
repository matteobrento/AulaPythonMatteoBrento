"""
Utilizzate la linear regression per analizzare il dataframe di esempio in cui abbiamo le Calorie bruciate 
in base al peso della persona che fa esercizio fisico con la montain bike, allenate l'algoritmo, testatelo e poi realizzate un grafico
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

df = pd.read_csv("C:\\Users\\matte\\AcademyItConsulting\\Esercitazioni\\25.07\\calories.csv")
print("Dataset Iniziale: \n", df, "\n")

calorie_X = df.iloc[:, 1].values.reshape(-1, 1) #iloc permette di accedere ai valori delle righe, qui selezioniamo kg e la rendiamo una colonna
print("Kg: \n", calorie_X, "\n") 
calorie_y = df.iloc[:, 2].values    #qui prendiamo le calorie
print("Calorie: \n", calorie_y, "\n")

X = df[["kg"]]  #oppure X = df["kg"].reshape(-1,1)
y = df["calories"]

calorie_X_train, calorie_X_test, calorie_y_train, calorie_y_test = train_test_split(
X, y, test_size=0.20)

""" calorie_X_train = calorie_X[:-20]   
calorie_X_test = calorie_X[-20:] """
print("X_train: \n", calorie_X_train, "\n")
print("X_test: \n", calorie_X_test, "\n")

""" calorie_y_train = calorie_y[:-20]
calorie_y_test = calorie_y[-20:] """
print("Y_train: \n", calorie_y_train, "\n")
print("Y_test: \n", calorie_y_test, "\n")

regressione = linear_model.LinearRegression()
regressione.fit(calorie_X_train, calorie_y_train)   #addestramento del modello su dati di train
calorie_y_pred = regressione.predict(calorie_X_test)    #predizione delle y tramite metodo predict sui dati di test

print("Coefficients: \n", regressione.coef_)
print("Mean squared error: %.2f" % mean_squared_error(calorie_y_test, calorie_y_pred))
print("Coefficient of determination: %.2f" % r2_score(calorie_y_test, calorie_y_pred))

plt.scatter(calorie_X_test, calorie_y_test, color="red")
plt.plot(calorie_X_test, calorie_y_pred, color="blue", linewidth=3)
plt.xticks(())
plt.yticks(())
plt.show()




