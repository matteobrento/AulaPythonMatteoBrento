"""
Create una classe calciatore che ha come attributi:
-nome:
-ruolo:
-valore.
Create un metodo getter per avere solo i valori dei calciatori e un metodo setter per settare il ruolo del calciatore.
Create almeno 3 calciatori e poi printate in ordine di valore i calciatori
"""

class Calciatore:

    def __init__(self, nome, ruolo, valore):
        self.nome = nome
        self.ruolo = ruolo
        self.valore = valore

    def __str__(self):  #posso trasformare gli elementi della classe in una stringa
        return f"Nome: {self.nome}, Ruolo: {self.ruolo}, Valore: {self.valore}"

    def visualizza_valore(self):
        return self.valore

    def inserisci_ruolo(self):
        self.ruolo = input("Inserisci il ruolo del calciatore: ")

c1 = Calciatore("Szczesny", "Portiere", "20")
c2 = Calciatore("Vlahovic", "Attaccante", "70")
c3 = Calciatore("Barella", "Centrocampista", "60")

print(c1.ruolo)

""" 
c1.visualizza_valore()
c2.visualizza_valore()
c3.visualizza_valore() 
"""

print("Lista dei calciatori completa: ")
print(c1)
print(c2)
print(c3)

# listaValori = [c1,c2,c3]
# print(listaValori)

lista = [c1.visualizza_valore(), c2.visualizza_valore(), c3.visualizza_valore()]
calciatori = [c1,c2,c3]
lista.sort(reverse=True)
print(lista)
print("\n")

for element in lista:
    for calciatore in calciatori:
        if calciatore.visualizza_valore() == element:
            print(calciatore)







