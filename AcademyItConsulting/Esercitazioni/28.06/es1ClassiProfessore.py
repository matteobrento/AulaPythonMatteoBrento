class Calciatore:
    ruoli = {"1":"portiere","2":"difensore","3":"centrocampista","4":"attaccante"}
    def __init__(self, nome, ruolo, valore):
        self.nome = nome
        self.ruolo = Calciatore.ruoli[ruolo]
        self.valore = valore
    
    def visualizza_valore(self):
        return self.valore
    
    def setta_ruolo(self, ruolo):
        self.ruolo = ruolo
    
    def __str__(self):
        return f"Nome: {self.nome}, Ruolo: {self.ruolo}, Valore: {self.valore}"

dizionario = {}
for i in range(3):
    nome = input("inserisci il nome: ")
    ruolo = input("inserisci il ruolo: ")
    valore = input("inserisci il valore: ")
    dizionario[int(valore)] = Calciatore(nome, ruolo, valore)

lista_ord = list(dizionario.keys())
lista_ord.sort(reverse=True)

for element in lista_ord:
    print(dizionario[element].visualizza_valore(),"\n\n", dizionario[element])