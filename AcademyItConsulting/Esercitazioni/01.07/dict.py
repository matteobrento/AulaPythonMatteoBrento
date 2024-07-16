class Piatto:

    menu = []

    def __init__(self, nome_piatto, prezzo):
        self.nome_piatto = nome_piatto
        self.prezzo = prezzo

    def aggiungi_al_menu(self):

        nome_piatto = input("Inserisci il nome del piatto: ")
        prezzo = input("Inserisci il prezzo: ")
        piatto = {"nome_piatto":nome_piatto, "prezzo":prezzo}
        Piatto.menu.append(piatto)
        print(Piatto.menu)
        print("Il piatto è stato aggiunto!")

    def togli_dal_menu(self):

        nome_piatto = input("Inserisci il nome del piatto che vuoi rimuovere: ")
        trovato = False
        for piatto in Piatto.menu:
            if piatto["nome_piatto"] == nome_piatto:
                Piatto.menu.remove(piatto)
                print(f"Prodotto {piatto['nome_piatto']} eliminato con successo!")
                trovato = True
                break
        
        if not trovato:
            print("Il piatto non è nel menù!")

    def stampa_menu(self):

        print(Piatto.menu)


aggiungi = aggiungi_al_menu()

