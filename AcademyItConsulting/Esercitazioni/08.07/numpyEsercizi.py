import numpy as np

"""
Creazione e Manipolazione degli Array:
- Crea un array di 10 elementi, tutti uguali a 5.
- Cambia la forma dell'array creato in una matrice 2x5.
- Crea un array di numeri casuali tra 0 e 1 di dimensione 4x4.
"""

print("ESERCIZIO 1 \n")
a = np.array([5,5,5,5,5,5,5,5,5,5])     #cercando in internet ci sono np.full/np.repeat (10,5) per automatizzarlo
a = np.array([5,5,5,5,5,5,5,5,5,5]).reshape(2,5)
print(a)
print("\n")
a_casuali = np.random.rand(4,4)
print(a_casuali)
print("\n")


"""
Operazioni sugli Array:
- Crea due array di dimensione 3x3 e calcola il loro prodotto elemento per elemento.
- Calcola la somma di tutti gli elementi di un array 3x3 creato con valori da 1 a 9.
"""

print("ESERCIZIO 2 \n")
b1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
b2 = np.array([[1,2,2],[2,3,4],[3,2,1]])
prodotto = b1*b2
print("Prodotto Elemento x Elemento: ", prodotto)
print("\n")
b = np.random.randint(1,9,size=(3,3))
print(b)
print("Somma: ", np.sum(b))
print("\n")


"""
Utilizzo delle Funzioni:
- Crea un array contenente 20 numeri equidistanti tra 0 e 10.
- Utilizza `numpy.random` per generare un array di numeri interi casuali tra 1 e 100 di dimensione 5x5.
"""

print("ESERCIZIO 3 \n")
c = np.linspace(0,10,20)
print(c)
print("\n")
c1 = np.random.randint(1,100,size=(5,5))
print(c1)
print("\n")


"""
Operazioni sugli Array:
- Crea un array di numeri casuali di dimensione 5x5 e calcola la media dei valori di ciascuna colonna.
- Crea un array di numeri casuali di dimensione 5x5 e calcola la somma dei valori di ciascuna riga.
"""

print("ESERCIZIO 4 \n")
matrice = np.random.randint(1,10,size=(5,5))
print(matrice)
print("\n")
print("Riga 0: ", matrice[0])
print("\n")

""" 
print(np.sum(matrice[0,:]))
print(np.sum(matrice[1,:]))   #somma riga per riga
print(np.sum(matrice[2,:])) 
"""

for riga in matrice:
    riga = print(np.sum(riga))

print("\n")
print("Colonna 0: ", matrice[:,0])
print("\n")
for colonna in range(matrice.shape[1]):
    colonna = print(np.mean(matrice[:,colonna]))

print("\n")


"""
Manipolazione degli Array:
- Crea un array 1D con 12 elementi e trasformalo in una matrice 3x4.
- Estrai la prima colonna dalla matrice creata e sostituiscila con un array di zeri.
"""

print("ESERCIZIO 5 \n")
array1D = np.arange(0,12).reshape(3,4)
print(array1D)
print("\n")
zeri = np.zeros((3))
array1D[:,0] = zeri
print("Matrice Modificata: \n", array1D)
print("\n")


"""
Utilizzo di Funzioni:
- Utilizza numpy.random per generare un array di numeri interi casuali tra 50 e 100 di dimensione 3x3. 
Trova il massimo e il minimo valore di questo array.
- Crea due array 1D di dimensione 5 con numeri casuali e trova il prodotto scalare tra i due.
"""

print("ESERCIZIO 6 \n")
casuale = np.random.randint(50,100,size=(3,3))
print(casuale)
print("\n")
massimo = np.max(casuale)
minimo = np.min(casuale)
print("Massimo: ", massimo)
print("Minimo: ", minimo)
print("\n")

a1D = np.random.randint(1,10,5)
a2D = np.random.randint(1,10,5)
print("Riga 1: ", a1D)
print("\n")
print("Riga 2: ", a2D)
print("\n")
scalare = np.inner(a1D,a2D) #metodo che calcola il prodotto scalare
print("Prodotto Scalare: ", scalare)





