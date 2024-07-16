class Animale:

    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = int(eta)

    def fai_suono(self):
        print(f"{self.nome} di {self.eta} anni fa il seguente verso: deckuverfuycye")


class Leone(Animale):

    def __init__(self, nome, eta, verso):
        super().__init__(nome, eta)
        self.verso = verso

    def fai_suono(self):
        print(f"{self.nome} di {self.eta} anni fa il seguente verso: {self.verso}")
    
    def caccia(self):
        print(f"{self.nome} il bro sta cacciando nella savana")


class Giraffa(Animale):

    def __init__(self, nome, eta, colore, verso):
        super().__init__(nome, eta)
        self.colore = colore
        self.verso = verso

    def fai_suono(self):
        print(f"{self.nome} di {self.eta} anni fa il seguente verso: {self.verso}")
    
    def mostra_colore(self):
        print(f"{self.nome} è di colore {self.colore}")


animale = Animale("animale casuale", 8)
animale.fai_suono()

leone = Leone("leopoldo", 13, "AAAARGH")
leone.fai_suono()
leone.caccia()

giraffa = Giraffa("lucia", 15, "giallo", "lololololololol")
giraffa.fai_suono()
giraffa.mostra_colore()

