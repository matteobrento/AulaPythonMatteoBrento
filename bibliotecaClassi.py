class Libro:
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    def descrizione(self):
        print(f"Il libro '{self.titolo}' è stato scritto da {self.autore} e ha {self.pagine} pagine")

class Biblioteca:

    libri = []

    def aggiungi_libro(self):
        titolo = input("Inserisci il titolo: ")
        autore = input("Inserisci l'autore: ")
        pagine = int(input("Inserisci il numero di pagine: "))
        libro = Libro(titolo, autore, pagine)
        Biblioteca.libri.append(libro)
        print("Libro aggiunto!")

    def mostra_libri(self):
        if not Biblioteca.libri:
            print("La biblioteca è vuota.")
        else:
            for libro in Biblioteca.libri:
                libro.descrizione()

biblioteca = Biblioteca()
while True:
    biblioteca.aggiungi_libro()
    biblioteca.mostra_libri()
    scelta = input("Vuoi aggiungere un altro libro ? ") 
    if scelta.lower() != "si":
        print("Programma terminato")
        break


