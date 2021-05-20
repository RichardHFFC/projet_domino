from Dominolib import DominoTwo
from Dominolib import DominoOne
from colors import bcolors
from fctdomino import *
from Castlelib import *
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

print(DominoOne(SPLIT1[0],SPLIT1[1]))
print(DominoTwo(SPLIT2[0],SPLIT2[1]))
