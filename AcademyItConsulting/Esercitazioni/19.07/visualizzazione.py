import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

figura = plt.rcParams['figure.figsize'] = [10,6] #dimensione predefinita delle figure
plt.rcParams['figure.dpi'] = 100    #risoluzione delle figure in DPI

plt.rcParams['figure.facecolor'] = 'white'  #colore di sfondo della figura

sns.set_theme(style="darkgrid") #tema di default di seaborn

data = np.random.normal(size=100)

""" 
sns.histplot(data, kde=True)
plt.title('Distribuzione dei dati')
plt.show()


x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]


plt.figure()
plt.plot(x, y)
plt.title('Grafico a Linee')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show() 
"""

""" 
vendite = [100, 200, 300, 400, 200, 150, 50]
giorni_della_settimana = [1, 2, 3, 4, 5, 6, 7]

plt.figure()
plt.plot(giorni_della_settimana, vendite)
plt.title('Tracciamento del numero di vendite in una settimana')
plt.xlabel('Asse dei giorni della settimana')
plt.ylabel('Asse delle vendite')
plt.show()

categories = ['A', 'B', 'C', 'D', 'E']
values = [3, 7, 2, 5, 8]

plt.figure()
plt.bar(categories, values, color="red")
plt.title('Grafico a Barre')
plt.xlabel('Categorie')
plt.ylabel('Valori')
plt.show() 
"""

""" 
data = np.random.randn(1000)    #random radn genera valori casuali con la distribuzione gaussiana (valori compresi tra -3 e 3)
print(data)

plt.figure()
plt.hist(data, bins=30, color="red")  #bin divide il totale dei miei valori in tot intervalli, in questo caso 30 per creare l'hist
plt.title('Istogramma')
plt.xlabel('Valori')
plt.ylabel('Frequenza')
plt.show() 
"""

x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, c=x)
plt.colorbar(label='X values')

plt.scatter(x,  y, c=y)
plt.colorbar(label='Y values')

plt.figure()
plt.scatter(x, y)
plt.title('Scatter Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()





