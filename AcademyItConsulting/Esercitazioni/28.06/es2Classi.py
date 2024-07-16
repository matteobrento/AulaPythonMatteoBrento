"""
Create un classe libro che ha al suo interno:
- titolo;
- autore;
- prezzo;
- codice isbn viene generato automaticamente in maniera randomica ogni volta che inserito un libro;
- stato_prestito;

Create poi 2 metodi:
- Metodo sconto per applicare lo sconto della percentuale passata al prezzo;
- Metodo prestito per cambiare lo stato del prestito, quindi se è libero diventa prestato, se è prestato diventa libero
"""
import random

class Libro:

    alfabeto = "abcdefghilmnopqrstuvwxyz"
    def __init__(self, titolo, autore, prezzo):
        self.titolo = titolo
        self.autore = autore
        self.prezzo = prezzo
        self.codice_isbn = random.choice(Libro.alfabeto).lower() + random.choice(Libro.alfabeto).lower() + str(random.randint(0,9)) + str(random.randint(0,9))
        self.stato_prestito = "libero"

    def inserisci_titolo(self):
        return self.titolo 
    
    def inserisci_autore(self):
        return self.autore 
    
    def inserisci_prezzo(self):
        return self.prezzo 
    
    def inserisci_codice_isbn(self):
        return self.codice_isbn
    
    def inserisci_stato(self):
        return self.stato_prestito
    
    def visualizza_titolo(self):
        print(self.titolo)
    
    def visualizza_autore(self):
        print(self.autore)

    def visualizza_prezzo(self):
        print(self.prezzo)

    def visualizza_codice(self):
        print(self.codice_isbn)

    def visualizza_stato(self):
        print(self.stato_prestito)
    
    def __str__(self):
        return f"Titolo: {self.titolo}, Autore: {self.autore}, Prezzo: {self.prezzo}, Codice ISBN: {self.codice_isbn}, Libero per prestito: {self.stato_prestito}"
    
    
dizionario = {}
for i in range(2):
    titolo = input("Inserisci il titolo: ")
    autore = input("Inserisci l'autore: ")
    prezzo = input("Inserisci il prezzo: ")
    codice_isbn = random.randint(0,100)
    stato_prestito = input("Inserisci lo stato del prestito: ")
    print("\n")

    dizionario[int(codice_isbn)] = Libro(titolo, autore, prezzo, codice_isbn, stato_prestito)

lista_ord = list(dizionario.keys())
for element in lista_ord:
    print(dizionario[element])