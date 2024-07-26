import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.model_selection import train_test_split


df = pd.read_csv("https://raw.githubusercontent.com/madmashup/targeted-marketing-predictive-engine/master/banking.csv")
print(df)

print(df["y"].value_counts(), "\n")
print(df.isnull().sum(), "\n")
print(df["job"].value_counts(), "\n")

def analisi_dati(df):

    df = df[df['job'] != 'unknown']
    
    def categoria(job):
        if job == "student" or job == "unemployed" or job == "housemaid":
            return 0
        elif job == "blue-collar" or job == "technician" or job == "services" or job == "self-employed":
            return 1
        elif job == "retired" or job == "entrepreneur"or job == "management" or job == "admin.":
            return 2
        else:
            return -1  

    df.loc[:,'job'] = df['job'].apply(categoria)

    def eta(valore):
        if valore<50:
            return 1
        else:
            return 0
        
    df.loc[:,'age'] = df['age'].apply(eta)

    def campaign(valore):
        if valore<3:
            return 1
        else:
            return 0
        
    df.loc[:,'campaign'] = df['campaign'].apply(campaign)

    df = df[(df['default'] != 'unknown') & (df['housing'] != 'unknown') & (df['loan'] != 'unknown')]

    df.loc[:, 'default'] = df['default'].map(lambda x: 1 if x == 'yes' else 0)
    df.loc[:, 'housing'] = df['housing'].map(lambda x: 1 if x == 'yes' else 0)
    df.loc[:, 'loan'] = df['loan'].map(lambda x: 1 if x == 'yes' else 0)

    print("DataFrame modificato: \n", df, "\n")
    return df

df = analisi_dati(df)

def regressione_logistica(df):

    print(df["job"].value_counts(), "\n")
    print(df["campaign"].value_counts(), "\n")
    print(df["age"].value_counts(), "\n")

    X = df[["age", "job", "default", "housing", "loan", "campaign", "emp_var_rate", "cons_price_idx", "cons_conf_idx", "euribor3m"]]
    print(X, "\n")
    y = df["y"]

    print(y, "\n")
    #print(X.shape)
    #print(y.shape)

    #dividiamo i dati in train e test
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    model = LogisticRegression(solver='liblinear', C=100, random_state=0).fit(X_train, y_train)
    predizione = model.predict(X_test)
    predizione_train = model.predict(X_train)
    score = model.score(X_train, y_train)
    print("Score: ", score, "\n")
    print("classi:", model.classes_, "\n")
    print("intercetta:", model.intercept_, "\n")
    print("coefficienti:", model.coef_, "\n")

    cm = confusion_matrix(y_train, predizione_train)
    print(cm, "\n")

    cm2 = confusion_matrix(y_test, predizione)
    print(cm2, "\n")

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(cm)
    ax.grid(False)
    ax.xaxis.set(ticks=(0, 1), ticklabels=('Predicted 0s', 'Predicted 1s'))
    ax.yaxis.set(ticks=(0, 1), ticklabels=('Actual 0s', 'Actual 1s'))
    ax.set_ylim(1.5, -0.5)
    for i in range(2):
        for j in range(2):
            ax.text(j, i, cm[i, j], ha='center', va='center', color='red')
    plt.show()

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(cm2)
    ax.grid(False)
    ax.xaxis.set(ticks=(0, 1), ticklabels=('Predicted 0s', 'Predicted 1s'))
    ax.yaxis.set(ticks=(0, 1), ticklabels=('Actual 0s', 'Actual 1s'))
    ax.set_ylim(1.5, -0.5)
    for i in range(2):
        for j in range(2):
            ax.text(j, i, cm2[i, j], ha='center', va='center', color='red')
    plt.show()

    print(classification_report(y_test, predizione))
    print("ROC AUC Score: ", roc_auc_score(y_test, model.predict_proba(X_test)[:,1]))

regressione_logistica(df)


