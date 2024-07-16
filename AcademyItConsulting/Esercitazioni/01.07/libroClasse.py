class Libro:

    def __init__(self, titolo, autore, pagine): #definizione del costruttore con self e i 3 attributi
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    def descrizione(self):  #metodo di stampa degli attributi in una stringa
        print("Il libro",self.titolo,"è stato scritto da",self.autore,"e ha",self.pagine,"pagine")


libro1 = Libro("Harry Potter", "Rowling", "300")    #creazione dell'oggetto libro1 di tipo Libro con i parametri passati
libro1.descrizione()    #funzione di stampa chiamata


class Biblioteca(Libro):
    
    def __init__(self, titolo, autore, pagine, codice):
        super().__init__(titolo, autore, pagine)
        self.codice = codice

    def stampa(self):
        return super().__str__,f", Codice: {self.codice}"
    

libro2 = Biblioteca("Harry Potter 2", "Rowling", "250", "0")
libro2.stampa()
    