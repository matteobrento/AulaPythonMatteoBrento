class Veicolo:

    def __init__(self, marca, modello, anno, accensione = False):
        self.__marca = marca
        self.__modello = modello
        self.__anno = int(anno)
        self.__accensione = accensione

    def accendi(self):
        if self.__accensione:
            self.__accensione = True
            print("Veicolo acceso!")

    def spegni(self):
        if self.__accensione == True:
            self.__accensione = False
            print("Veicolo Spento!")

    #METODI GET E SET PRIVATI UTILIZZABILI SOLO DAL GESTORE

    def __get_marca(self):
        return self.__marca
    
    def __set_marca(self, marca):
        self.__marca = marca

    def __get_modello(self):
        return self.__modello
    
    def __set_modello(self, modello):
        self.__modello = modello

    def __get_anno(self):
        return self.__anno
    
    def __set_anno(self, anno):
        self.__anno = anno

    def __get_accensione(self): #metodo di accesso allo stato di accensione accessibile solo dal gestore
        return self.__accensione
    
    def __set_accensione(self, accensione): #metodo di modifica dello stato di accensione accessibile solo dal gestore
        self.__accensione = accensione


class Auto(Veicolo):

    veicolo = "Auto"

    def __init__(self, marca, modello, anno, numero_porte, accensione=False):
        super().__init__(marca, modello, anno, accensione)
        self.__numero_porte = numero_porte

    def suona_clacson(self):
        print("Popi popi")

    def __get_numero_porte(self):
        return self.__numero_porte
    
    def __set_numero_porte(self, numero_porte):
        self.__numero_porte = numero_porte


class Furgone(Veicolo):

    veicolo = "Furgone"

    def __init__(self, marca, modello, anno, capacita_carico, accensione=False):
        super().__init__(marca, modello, anno, accensione)
        self.__capacita_carico = capacita_carico
        self.__carico_attuale = 0

    def carica(self, merce):
        
        if self.__carico_attuale + merce > self.__capacita_carico:
            print("Capienza massima superata")
        else:
            self.__capacita_carico += merce
            self.__carico_attuale += merce
            print(f"Merce caricata: {merce}. Carico attuale: {self.__carico_attuale}")

    def scarica(self, merce):

        if self.__carico_attuale - merce < self.__capacita_carico:
            print("Scarico possibile!")
            self.__carico_attuale -= merce
            print(f"Merce scaricata: {merce}. Carico attuale: {self.__carico_attuale}")
        else:
            print("Stai provando a scaricare una quantità maggiore! Errore!")

    def __get_capacita_carico(self):
        return self.__capacita_carico
    
    def __set_capacita_carico(self, capacita_carico):
        self.__capacita_carico = capacita_carico


class Motocicletta(Veicolo):

    veicolo = "Motocicletta"

    def __init__(self, marca, modello, anno, tipo, accensione=False):
        super().__init__(marca, modello, anno, accensione)
        self.__tipo = tipo
    
    def esegui_wheelie(self):
        if self.__tipo == "sportivo":
            print("Impenna!")
        else:
            print("Non azzardarti ad impennare che non te la fidi!")

    def __get_tipo(self):
        return self.__tipo
    
    def __set_tipo(self, tipo):
        self.__tipo = tipo


class Gestore(Veicolo):

    def __init__(self):

        self.__veicoli == []
        self.__tipoVeicolo == {"Auto":0, "Furgone":0, "Motocicletta":0}

    def set_accensione(self, veicolo, accensione):
        veicolo.__set_accensione(accensione)

    



""" 
furgone = Furgone("Audi", "P7", 2008, 1500)
furgone.carica(1000)
furgone.scarica(800) 
"""
        


    
    