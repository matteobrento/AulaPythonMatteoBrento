class Studenti:
    corpo_studentesco = 0
    ore_settimanali = 36
    def __init__(self, nome, cognome, voti):    #self per ogni volta che viene creato un oggetto di tipo studente lo richiama
        self.nome = nome
        self.cognome = cognome
        self.voti = voti
        Studenti.corpo_studentesco += 1 

    def __str__(self):  #posso trasformare gli elementi della classe in una stringa
        return f"Nome: {self.nome}, Cognome: {self.cognome}, Voti: {self.voti}, Ore Settimanali: {self.ore_settimanali}"
    
    
    def visualizza_nome(self):  #anche i metodi non costruttori hanno self
        print(self.nome)    #metodo getter, restituisce un valore dall'interno della nostra classe


    def inserisci_nome(self):   #metodo setter
        self.nome = input("Inserisci il nome: ")

s1 = Studenti("Matteo", "Brento", [9,7])
s2 = Studenti("Marco", "Rossi", [5,8])  
s3 = Studenti("Giovanni", "Neri", [6,9])
print(s1.nome)  #stampa l'istanza passata
print(s2.voti)
s1.visualizza_nome()    #i metodi che facciamo vanno chiamati con classe.metodo

s1.ore_settimanali += 4 #aggiunge 4 ore settimanali allo studente s1
print(s1)

s2.ore_settimanali -= 10
print(s2)

print(Studenti.corpo_studentesco)   #tiene il count degli oggetti studente
