"""
Utilizzate la linear regression per analizzare il dataframe di esempio con Fabbisogno calorico giornaliero di un uomo 
in base alla sua età, allenate l'algoritmo, testatelo e poi realizzate un grafico.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

df = pd.read_csv("C:\\Users\\matte\\AcademyItConsulting\\Esercitazioni\\25.07\\fabbisogno calorico.csv")
df = df.drop(df.columns[0], axis=1)
print("Dataset Iniziale: \n", df, "\n")

X = df[["età"]]
""" 
X = df["età"]
X = X.values[:,np.newaxis] 
"""
#X = df.iloc[:, 1].values.reshape(-1,1)
y = df["calories"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

print("X_train: \n", X_train, "\n")
print("X_test: \n", X_test, "\n")
print("Y_train: \n", y_train, "\n")
print("Y_test: \n", y_test, "\n")

reg = linear_model.LinearRegression()
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)

print("Coefficients: \n", reg.coef_)
print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))
print("Coefficient of determination: %.2f" % r2_score(y_test, y_pred))

plt.scatter(X_test, y_test, color="red")
plt.plot(X_test, y_pred, color="blue", linewidth=3)
plt.xticks(())
plt.yticks(())
plt.show()
