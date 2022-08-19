# Simulazione esselunga                          -by Giovanni Grassi

def prod():
    
    prodotti = {"Acqua" : [1, "/ //", "Bottiglia di aqua naturale da 500ml"], 
                "Burro" : [3, "// //", "Panetto di burro da 250g"],
                "Coca-cola" : [2 , "/// /", "Bottiglia di coca cola da 660 ml"]}
         
    return prodotti    

def esamina():
    prodotti = prod()
    c = True
    
    print("Prodotti disponibili:", prodotti.keys())
    
    while c == True:
            print(prodotti.get(input("Quale prodotto vuoi esaminare? ")))
            
            sn = input("Vuoi esaminare altri prodotti? ")
            
            if sn == "si" or sn == "no":
                
                c = False
                
                if sn == "si":
                    c = True
                
                if sn == "no":
                    print()
                    
            else: print("/Errore/ per favore inserisci si o no")
        
    
def aCarrello():
    prodotti = prod()
    carrello = {}
    c = True
    
    print("Prodotti disponibili:", prodotti.keys())
    
    while c == True:
        
        p = input("Quale prodotto vuoi aggiungere al carrello? ")
        
        if prodotti.get(p) != None :
            
            carrello[p] = prodotti.get(p)
            
            print("Prodotto aggiunto correttamente")
            
        else: print("Prodotto inesistente")
        
        
        sn = input("Vuoi aggiungere al carrello altri prodotti? ")
        
        if sn == "si" or sn == "no":
            
            c = False
            
            if sn == "si":
                c = True
            
            if sn == "no":
                print()
                
        else: print("/Errore/ per favore inserisci si o no")
        
    return carrello

def cassaManuale(carrello):
    
    p = 0

def cassaAuto(carrello):
    
    p = 0
    
    k = False
    
    for i in carrello:
        
        p += carrello.get(i)[0]
        
    if p > 500:
        
        print("Hai superato il budget!")
    
    else: k = True
    
    if k == True:
        print("Grazie di aver aquistato qua, a presto")
        
    
def main():
    tut = True
    
    carrello = {}
    
    budget = 500
    
    while tut == True:
        
        c = True
        
        print("\nBenvenuto all'esselunga \nOgni prodotto ha assegnato a esso il prezzo un codice a barre e una breve descrizione \nHai 500€ di budget, divertiti")
        
        while c == True:

            op = int(input("\n\nSeleziona: \n1-Esamina prodotto \n2-Aggiungi un prodotto al carrello \n3-Visualizza il contenuto del carrello \n4-Vai alla cassa \n\n-"))
            
            if op > 0 and op < 5:
                
                if op == 1:
                    esamina()
                    
                if op == 2:
                    carrello = aCarrello()
                    
                if op == 3:
                    print("Carrello:", carrello)
                    
                if op == 4:
                    c = False
        
        t = True
        
        while t == True:
            
            cs = int(input("\nSeleziona: \n1-Cassa self-service \n2-Cassa automatica  \n\n-"))
            
            if cs > 0 and cs < 3:
            
                if cs == 1:
                    cassaManuale(carrello)
                    t = False
                    tut = False
                    
                if cs == 2:
                    cassaAuto(carrello)
                    t = False
                    tut = False
main()
    