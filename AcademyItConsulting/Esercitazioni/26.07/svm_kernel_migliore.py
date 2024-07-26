"""
L'obiettivo di questo esercizio è identificare il kernel migliore dell'algoritmo SVM per classificare il tipo di fiore 
"setosa" e "virginica" del dataset iris.
Di seguito la base per importare il dataset e le classi specifiche
"""

from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.svm import SVC 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()
#print("DataFrame Iris: \n", iris, "\n")
X = iris.data
y = iris.target

X = X[y != 1, :2]
y = y[y != 1]

#grafico per vedere il dataset nella totalità

_, ax = plt.subplots()
scatter = ax.scatter(iris.data[:, 0], iris.data[:, 1], c=iris.target)
ax.set(xlabel=iris.feature_names[0], ylabel=iris.feature_names[1])
_ = ax.legend(
    scatter.legend_elements()[0], iris.target_names, loc="lower right", title="Classes"
)
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

model = SVC(kernel='linear', C=1E10)
model.fit(X_train, y_train)

#SVC divisione

def plot_svc_decision_function(model, ax=None, plot_support=True):
    if ax is None:
        ax = plt.gca()
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    
    # create grid to evaluate model
    x = np.linspace(xlim[0], xlim[1], 30)
    y = np.linspace(ylim[0], ylim[1], 30)
    Y, X = np.meshgrid(y, x)
    xy = np.vstack([X.ravel(), Y.ravel()]).T
    P = model.decision_function(xy).reshape(X.shape)
    
    # plot decision boundary and margins
    ax.contour(X, Y, P, colors='k',
               levels=[-1, 0, 1], alpha=0.5,
               linestyles=['--', '-', '--'])
    
    # plot support vectors
    if plot_support:
        ax.scatter(model.support_vectors_[:, 0],
                   model.support_vectors_[:, 1],
                   s=300, linewidth=1, facecolors='none')
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)

#creiamo il grafico
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn',edgecolors='black')
#richiamimamo la funzione
plot_svc_decision_function(model)


kernel_linear = 'linear'
model_linear = SVC(kernel=kernel_linear, C=1E10)
model_linear.fit(X_train, y_train)
y_pred_linear = model_linear.predict(X_test)
score_linear = accuracy_score(y_test, y_pred_linear)

plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn', edgecolors='black')
plot_svc_decision_function(model_linear)
plt.title(f'SVC con kernel {kernel_linear}')
plt.show()

kernel_rbf = 'rbf'
model_rbf = SVC(kernel=kernel_rbf, C=1E10)
model_rbf.fit(X_train, y_train)
y_pred_rbf = model_rbf.predict(X_test)
score_rbf = accuracy_score(y_test, y_pred_rbf)

plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn', edgecolors='black')
plot_svc_decision_function(model_rbf)
plt.title(f'SVC con kernel {kernel_rbf}')
plt.show()

kernel_poly = 'poly'
model_poly = SVC(kernel=kernel_poly, C=1E10)
model_poly.fit(X_train, y_train)
y_pred_poly = model_poly.predict(X_test)
score_poly = accuracy_score(y_test, y_pred_poly)

plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='autumn', edgecolors='black')
plot_svc_decision_function(model_poly)
plt.title(f'SVC con kernel {kernel_poly}')
plt.show()

print(f'Accuratezza per kernel {kernel_linear}: {score_linear}')
print(f'Accuratezza per kernel {kernel_rbf}: {score_rbf}')
print(f'Accuratezza per kernel {kernel_poly}: {score_poly}')












