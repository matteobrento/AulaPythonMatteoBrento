"""
Create tre classi:
- classe madre mezzo;
- Classe figlio moto;
- Classe figlio auto.
"""

class Mezzo:

    def __init__(self, nome, targa):
        self.nome = nome
        self.targa = targa

    def __str__(self):
        return f"Nome: {self.nome}, Targa: {self.targa}"
    

class Moto(Mezzo):

    def __init__(self, nome, targa, modello):
        super().__init__(nome, targa)
        self.modello = modello

    def __str__(self):
        return super().__str__()+f", Ruolo: {self.modello}"
    
class Auto(Mezzo):
    
    def __init__(self, nome, targa, cilindrata):
        super().__init__(nome, targa)
        self.cilindrata = cilindrata

    def __str__(self):
        return super().__str__()+f", Ruolo: {self.cilindrata}"
    

mezzo = Mezzo("Camion", "123abc")
moto = Moto("Moto", "456abd", "supersport")
auto = Auto("Audi a1", "786bcd", "1200")

