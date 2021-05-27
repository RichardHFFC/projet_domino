from Dominolib import DominoTwo
from Dominolib import DominoOne
from fctdomino import DOMINO_24, DRAW, draw, Split1, Split2, print_board
from colors import bcolors
from Board_player import Player, Castle, Dom
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

while True:
    numbertuile= int(input("Enter num tuile : "))
    if numbertuile < 4:
        break

print("")
SPLIT1=Split1(DRAW,numbertuile)
#print(SPLIT1)
print("")

SPLIT2=Split2(DRAW,numbertuile)
#print(SPLIT2)
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
        Dom1 = SPLIT1
        Dom2 = SPLIT2
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
        Dom1 = SPLIT2
        Dom2 = SPLIT1
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


a = [[0, 0, 7, 0, 4, 0, 2, 2, 2, 1 ], [1, 1, 2, 3, 4, 0, 2, 2, 2, 1 ], [1, 1, 2, 3, 4, 0, 2, 2, 2, 1 ], [1, 1, 2, 3, 4, 0, 2, 2, 2, 1 ], [1, 1, 2, 3, 4, 0, 2, 2, 2, 1 ]]

print_board(a)

print(a[0])
print("")
(a[0][0])= SPLIT1[0]
(a[0][1])= SPLIT1[1]
print(a[0])

print_board(a)
P1=Player(1)
P2=Player(2)
"""
print_board(P1.a)
print("")
(P1.a[0][0])= SPLIT1[0]
print_board(P1.a)
print("")
"""
while True:
    board = int(input("what is your board (1,2) : "))
    if (board == 1):
        board = P1.a
        break
    if (board == 2):
        board = P1.b
        break
while True:
    line = int(input("what is your line (1,2,3,4,5) : "))
    if ((line == 1)or(line == 2)or(line == 3)or(line == 4)or(line == 5)):
        break
while True:
    colum = int(input("what is your column (1,2,3,4,5) : "))
    if ((colum == 1)or(colum == 2)or(colum == 3)or(colum == 4)or(colum == 5)):
        break
Castle(line,colum,board)
print_board(board)
print("")

while True:
    board = int(input("what is your board (1,2) : "))
    if (board == 1):
        board = P1.a
        break
    if (board == 2):
        board = P1.b
        break
while True:
    line = int(input("what is your line (1,2,3,4,5) : "))
    if ((line == 1)or(line == 2)or(line == 3)or(line == 4)or(line == 5)):
        break
while True:
    colum = int(input("what is your column (1,2,3,4,5) : "))
    if ((colum == 1)or(colum == 2)or(colum == 3)or(colum == 4)or(colum == 5)):
        break
Dom(line,colum,board,Dom1)
if localisationTuile == 2 :
    Dom(line+1,colum,board,Dom2)
elif localisationTuile == 4 :
    Dom(line,colum-1,board,Dom2)
elif localisationTuile == 6 :
    Dom(line,colum+1,board,Dom2)
elif localisationTuile == 8 :
    Dom(line-1,colum,board,Dom2)

#Castle(line,colum,board)
print(board)
print_board(board)
print("")