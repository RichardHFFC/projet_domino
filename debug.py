from numpy.core.fromnumeric import shape
from Dominolib import DominoTwo
from Dominolib import DominoOne
from fctdomino import DOMINO_24, DRAW, draw, Split1, Split2
from colors import bcolors

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
while True:
    numbertuile= int(input("Enter num tuile : "))
    if numbertuile < 4:
        break

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

while True:
    print("landOne = 0 and landTwo = 1")
    print("")
    numberTuile = int(input("what is your choice 0 or 1 : "))
    print("")
    #landOne fixe
    if numberTuile == 0:
        #landTwo localisation
        while True:
            localisationTuile = int(input("what is your choice 2 or 4 or 6 or 8 : "))
            if localisationTuile == 2:
                print(DominoOne(SPLIT1[0], SPLIT1[1]))
                print(DominoTwo(SPLIT2[0], SPLIT2[1]))
                break
            elif localisationTuile == 4:
                print(DominoTwo(SPLIT2[0], SPLIT2[1]), DominoOne(SPLIT1[0], SPLIT1[1])) 
                break
            elif localisationTuile == 6:
                print(DominoOne(SPLIT1[0], SPLIT1[1]), DominoTwo(SPLIT2[0], SPLIT2[1])) 
                break
            elif localisationTuile == 8:
                print(DominoTwo(SPLIT2[0], SPLIT2[1])) 
                print(DominoOne(SPLIT1[0], SPLIT1[1]))
                break
        break
    #landTwo fixe
    elif numberTuile == 1:
        while True:
        #landOne localisation
            localisationTuile = int(input("what is your choice 2 or 4 or 6 or 8 : "))
            if localisationTuile == 2:
                print(DominoTwo(SPLIT2[0], SPLIT2[1])) 
                print(DominoOne(SPLIT1[0], SPLIT1[1]))
                break
            elif localisationTuile == 4:
                print(DominoOne(SPLIT1[0], SPLIT1[1]), DominoTwo(SPLIT2[0], SPLIT2[1])) 
                break
            elif localisationTuile == 6:
                print(DominoTwo(SPLIT2[0], SPLIT2[1]), DominoOne(SPLIT1[0], SPLIT1[1])) 
                break
            elif localisationTuile == 8:
                print(DominoOne(SPLIT1[0], SPLIT1[1]))
                print(DominoTwo(SPLIT2[0], SPLIT2[1]))
                break
        break
print("")
"""
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
                plateau += str(DominoOne(SPLIT1[i], SPLIT1[j]))
            plateau += "|\n" + ligneComplete
        print(plateau)"""
#__Str__()
"""
BOARD = np.empty((5,5,2),dtype=int)
#for i in range(50):
#    BOARD = np.append(BOARD,np.zeros((1)),axis = 0)
#BOARD = BOARD.reshape(5,10)
print("")
print(BOARD)
BOARD[2,4]=SPLIT1[0]
BOARD[2,5]=SPLIT1[1]
print("")
print(BOARD)
print("")
print(DominoOne(int(BOARD[2,4]),int(BOARD[2,5])))
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
"""
"""for k in range(5):
    print(plateau)
    for i in range(0,BOARD.shape[0]):
        for j in range(0,BOARD.shape[1]):
            print(DominoOne(int(BOARD[j,i]),int(BOARD[j,i+1])))
        i = i+2
print(plateau)"""

croisement = "+"
ligne = "-"
ligneComplete = croisement
colonne = 0
while(colonne < 5) :
    for j in range (4): 
        ligneComplete += ligne
    ligneComplete += croisement  
    colonne = colonne + 1 
#ligneComplete += "\n" 


a = [[1, 1, 0, 0, 4, 0, 2, 2, 2, 1 ], [1, 1, 2, 3, 4, 0, 2, 2, 2, 1 ], [1, 1, 2, 3, 4, 0, 2, 2, 2, 1 ], [1, 1, 2, 3, 4, 0, 2, 2, 2, 1 ], [1, 1, 2, 3, 4, 0, 2, 2, 2, 1 ]]

for i in range(len(a)):
    for j in range(len(a[i])):
        if (j % 2) == 0:
            if a[i][j] != 0:
                print((DominoOne((a[i][j]), (a[i][j+1]))), end='')
            elif a[i][j] == 0:
                print("    ", end='')
    print()
