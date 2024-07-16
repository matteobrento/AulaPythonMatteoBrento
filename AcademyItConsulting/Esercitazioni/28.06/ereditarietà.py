class Persona:
    def __init__(self,nome,cognome):
        self.nome = nome
        self.cognome = cognome
    
    def __str__(self):
        return f"Nome: {self.nome}, Cognome: {self.cognome}"

class Calciatore(Persona):
    def __init__(self, nome, cognome, ruolo):
        super().__init__(nome, cognome)
        self.ruolo = ruolo
    
    def __str__(self):
        return super().__str__()+ f", Ruolo: {self.ruolo}" 

class Allenatore(Persona):
    def __init__(self, nome, cognome, patentino):
        super().__init__(nome, cognome)
        self.patentino = patentino
    
    def __str__(self):
        return super().__str__()+ f", Patentino: {self.patentino}"
    
antonio = Persona("Antonio","Rossi")

buffon = Calciatore("Gianluigi","Buffon","Portiere")

conte = Allenatore("Antonio","Conte", "Patentino uefa")

print(antonio)
print(buffon)
print(conte)