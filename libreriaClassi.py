class Libro:

    def __init__(self, titolo, autore, isbn):
        self.titolo = titolo
        self.autore = autore
        self.isbn = isbn

    def descrizione(self):  
        print("Il libro:",self.titolo,"scritto da:",self.autore,"ha il seguente codice isbn:",self.isbn)


class Libreria:

    def __init__(self):
        self.catalogo = []

    def aggiungi_libro(self):

        titolo = input("Inserisci il titolo del libro: ")
        autore = input("Inserisci l'autore del libro: ")
        isbn = input("Inserisci il codice isbn del libro: ")
        libro = Libro(titolo,autore,isbn)
        self.catalogo.append(libro)
        print("Il libro è stato aggiunto al catalogo correttamente! ")
        print(self.catalogo)

    def rimuovi_libro(self):

        isbn = input("Inserisci l'isbn del libro che vuoi rimuovere: ")
        trovato = False
        for libro in self.catalogo:
            if libro.isbn == isbn:
                self.catalogo.remove(libro)
                print("Libro rimosso correttamente! ")
                trovato = True
                break

        if not trovato:
            print("Il libro non è presente nel catalogo.")

        print(self.catalogo)

    def cerca_per_titolo(self):
        titolo = input("Inserisci il titolo: ")
        libriTrovati = []
        for libro in self.catalogo:
            if libro.titolo == titolo:
                libriTrovati.append(libro)
        if libriTrovati:
            for libro in libriTrovati:
                print(libro.descrizione())

    def mostra_catalogo(self):

        if self.catalogo:
            for libro in self.catalogo:
                print(libro.descrizione())
        else:
            print("Non ci sono libri nel catalogo.")


libreria = Libreria()
print("Aggiungi un libro:")
libreria.aggiungi_libro()
print("\n")
print("Cerca per libro per titolo: ")
libreria.cerca_per_titolo()
print("\n")
print("Rimuovi un libro: ")
libreria.rimuovi_libro()
print("\n")
print("Mostra il catalogo dei libri: ")
libreria.mostra_catalogo()


