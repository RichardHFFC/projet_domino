from Dominolib import DominoTwo
from Dominolib import DominoOne
from colors import bcolors
from fctdomino import *
from Castlelib import *
import numpy as np
print(f"{bcolors.GREEN}*************************************")
print("*  Affichage liste Domino mélangée  *")
print(f"*************************************{bcolors.BASE}")

for k in range(len(DOMINO_24)):
    print(DOMINO_24[k])

print(f"{bcolors.GREEN}***********************************")
print("*    Fin liste Domino mélangée    *")
print(f"***********************************{bcolors.BASE}")

print(" ")
print(f"taille liste : {len(DOMINO_24)}")
print(" ")

draw(DOMINO_24)

print(f"{bcolors.GREEN}*************************************")
print("*  Affichage liste Domino mélangée  *")
print(f"*************************************{bcolors.BASE}")

for k in range(len(DRAW)):
    print(DRAW[k])
"""
print(f"{bcolors.GREEN}***********************************")
print("*    Fin liste Domino mélangée    *")
print(f"***********************************{bcolors.BASE}")

print(" ")
print(f"taille liste : {len(DRAW)}")
print(" ")

for k in range(len(DOMINO_24)):
    print(DOMINO_24[k])

print(f"{bcolors.GREEN}***********************************")
print("*    Fin liste Domino mélangée    *")
print(f"***********************************{bcolors.BASE}")

print(" ")
print(f"taille liste : {len(DOMINO_24)}")
print(" ")

print(f"{bcolors.GREEN}*************************************")
print("*  Affichage liste Domino mélangée  *")
print(f"*************************************{bcolors.BASE}")

for k in range(len(KING)):
    print(KING[k])

print(f"{bcolors.GREEN}***********************************")
print("*    Fin liste Domino mélangée    *")
print(f"***********************************{bcolors.BASE}")

print(" ")
print(f"taille liste : {len(KING)}")
print(" ")
"""
numbertuile= int(input("Enter num tuile : "))
#print("num tuile is: " + numbertuile)
#print(DOMINO[numbertuile])
print("")
SPLIT1=Split1(DRAW,numbertuile)
#for k in range(len(SPLIT1)):
print(SPLIT1)
print("")

SPLIT2=Split2(DRAW,numbertuile)
print(SPLIT2)
print("")
print(DRAW[numbertuile])
print("")

print("landOne = 0 and landTwo = 1")
print("")
numberTuile = int(input("what is your choice 0 or 1 : "))
print("")
#landOne fixe
if numberTuile == 0:
    #landTwo localisation
    localisationTuile = int(input("what is your choice 2 or 4 or 6 or 8 : "))
    if localisationTuile == 2:
        print(DominoOne(SPLIT1[0], SPLIT1[1]))
        print(DominoTwo(SPLIT2[0], SPLIT2[1]))
    elif localisationTuile == 4:
        print(DominoTwo(SPLIT2[0], SPLIT2[1]) + DominoOne(SPLIT1[0], SPLIT1[1])) 
    elif localisationTuile == 6:
        print(DominoOne(SPLIT1[0], SPLIT1[1]) + DominoTwo(SPLIT2[0], SPLIT2[1])) 
    elif localisationTuile == 8:
        print(DominoTwo(SPLIT2[0], SPLIT2[1])) 
        print(DominoOne(SPLIT1[0], SPLIT1[1]))
#landTwo fixe
elif numberTuile == 1:
    #landOne localisation
    localisationTuile = int(input("what is your choice 2 or 4 or 6 or 8 : "))
    if localisationTuile == 2:
        print(DominoTwo(SPLIT2[0], SPLIT2[1])) 
        print(DominoOne(SPLIT1[0], SPLIT1[1]))
    elif localisationTuile == 4:
        print(DominoOne(SPLIT1[0], SPLIT1[1]), DominoTwo(SPLIT2[0], SPLIT2[1])) 
    elif localisationTuile == 6:
        print(DominoTwo(SPLIT2[0], SPLIT2[1]), DominoOne(SPLIT1[0], SPLIT1[1])) 
    elif localisationTuile == 8:
        print(DominoOne(SPLIT1[0], SPLIT1[1]))
        print(DominoTwo(SPLIT2[0], SPLIT2[1]))
print("")

def  __Str__():         
        croisement = "+"
        ligne = "-"
        
        ligneComplete = croisement
        colonne = 0
        while(colonne < 5) :
            for j in range (7): 
                ligneComplete += ligne
            ligneComplete += croisement  
            colonne = colonne + 1 
        ligneComplete += "\n" 

        plateau = ligneComplete 
        for i in range (5) :
            for j in range (5) : 
                plateau += "|"
                plateau += "   X   "
            plateau += "|\n" + ligneComplete
        print(plateau)
__Str__()

BOARD =[]
for i in range(50):
    BOARD = np.append(BOARD,np.zeros((1)),axis = 0)
BOARD = BOARD.reshape(5,10)
print("")
print(BOARD)
BOARD[2,4]=SPLIT1[0]
BOARD[2,5]=SPLIT1[1]
print("")
print(BOARD)
print("")
#print(DominoOne(int(BOARD[2,4]),int(BOARD[2,5])))
croisement = "+"
ligne = "-"
ligneComplete = croisement
colonne = 0
while(colonne < 5) :
    for j in range (7): 
        ligneComplete += ligne
    ligneComplete += croisement  
    colonne = colonne + 1 
ligneComplete += "\n" 
plateau = ligneComplete 

for k in range(5):
    print(plateau)
    for i in range (8):
        for j in range(5):
            print(DominoOne(int(BOARD[j,i]),int(BOARD[j,i+1])))
        i = i+2
print(plateau)