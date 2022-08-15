# -*- coding: utf-8 -*-

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
        
        if prodotti.get(p) == None :
            print("Prodotto inesistente")
        else: carrello[p] = prodotti.get(p), print("Prodotto aggiunto correttamente")
        
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
    print()
def cassaAuto(carrello):
    print()    
    
def main():
    
    carrello = {}
    
    budget = 500
    
    c = True
    
    print("\nBenvenuto all'esselunga \nOgni prodotto ha assegnato a esso il prezzo un codice a barre e una breve descrizione \nHai 500€ di budget, divertiti")
    
    while c == True:
             
        print("\n\nSeleziona: \n1-Esamina prodotto \n2-Aggiungi un prodotto al carrello \n3-Visualizza il contenuto del carrello \n4-Vai alla cassa")
        
        op = int(input("-"))
        
        if op > 0 and op < 5:
            
            if op == 1:
                esamina()
                
            if op == 2:
                carrello = aCarrello()
                
            if op == 3:
                print("Carrello:", carrello)
                
            if op == 4:
                c = False
        
    
main()
    