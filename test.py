from numpy import zeros,array
def  __Str__():         
        croisement = "+"
        ligne = "-"
        
        ligneComplete = croisement
        colonne = 0
        while(colonne < 5) :
            for j in range (10): 
                ligneComplete += ligne
            ligneComplete += croisement  
            colonne = colonne + 1 
        ligneComplete += "\n" 

        plateau = ligneComplete 
        for i in range (5) :
            for j in range (5) : 
                plateau = plateau +"|" +"     X    "
            plateau += "|\n" + ligneComplete
        print(plateau)
__Str__()

"""
System.out.print("Joueur " 
                                + joueur.getNomCouleurJoueurs() 
                                + " : veuillez choisir une case : ");
                    positionTab = clavier.nextInt();
                    xDest = (positionTab % 10)-1;
                    yDest = (positionTab / 10)-1;
"""

matrice = array([[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]])
print(matrice)
print("")
#matrice = matrice.reshape(5,5)
#print(matrice)
#print("")
"""
for i in range(0,25):
    for j in range(0,2):
        print(str(matrice[i][j]),", ")
    print()
"""
for ligne in matrice: #pour chaque ligne de la matrice
       for elt in ligne: #pour chaque élément de la ligne
          print(elt, end=", ")
       print()
