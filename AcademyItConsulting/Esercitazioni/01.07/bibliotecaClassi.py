class Libro:
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    def descrizione(self):
        print(f"Il libro '{self.titolo}' è stato scritto da {self.autore} e ha {self.pagine} pagine")

class Biblioteca:

    libri = []  #creo una lista vuota

    def aggiungi_libro(self):   #chiedo in input gli attributi
        titolo = input("Inserisci il titolo: ")
        autore = input("Inserisci l'autore: ")
        pagine = int(input("Inserisci il numero di pagine: "))
        libro = Libro(titolo, autore, pagine)   #creo una variabile libro con all'interno l'oggetto Libro
        Biblioteca.libri.append(libro)  #faccio un append del libro nella lista
        print("Libro aggiunto!")

    def mostra_libri(self):
        if not Biblioteca.libri:    #controllo se è vuota
            print("La biblioteca è vuota.")
        else:
            for libro in Biblioteca.libri:  #stampo il libro con il metodo descrizione() di libro
                libro.descrizione()

biblioteca = Biblioteca()   #ciclo While per inserirne piu di uno
while True:
    biblioteca.aggiungi_libro()
    biblioteca.mostra_libri()
    scelta = input("Vuoi aggiungere un altro libro ? ") 
    if scelta.lower() != "si":
        print("Programma terminato")
        break


