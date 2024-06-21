controllo = True
while controllo == True:
        
        e1 = int(input("Indicare estremo sinistro: "))      #estremo destro
        e2 = int(input("Indicare estremo destro: "))        #estremo sinistro
        n = int(input("Indicare con 0 i numeri primi, 1 altrimenti: "))  #scegliere opzione
        if n == 0:
            for i in range(e1,e2+1):    #scelta 0, numeri primi
                if i%2 !=0:
                    print(i)         
        elif n == 1:
            for i in range(e1,e2+1):    #scelta 1, numeri non primi
                if i%2 ==0:
                    print(i)
        else:
            print("L'opzione scelta non è valida")

        controllo = False