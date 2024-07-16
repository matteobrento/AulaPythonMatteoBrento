class Punto:

    x = 0   #creo le mie coordinate
    y = 0

    def __init__(self):
        pass

    def muovi(self, dx, dy):
        self.x = dx
        self.y = dy
    
    def distanza(self):
        if self.x>0 and self.y>0:
            print("La distanza da 0 è: ",self.x,self.y)
        elif self.x>0 and self.y<0:
            print("La distanza da 0 è: ",self.x,self.y)
        elif self.x<0 and self.y>0:
            print("La distanza da 0 è: ",self.x,self.y)
        elif self.x<0 and self.y<0:
            print("La distanza da 0 è: ",self.x,self.y)
        else:
            print("Le coordinate sono entrambe 0")

punto1 = Punto()
punto1.muovi(-2,5)
punto1.distanza()