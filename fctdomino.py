from listDomino import DOMINO
from Dominolib import DominoOne, DominoTwo
# Sélection des 24 premiers dominos
DOMINO_24 = DOMINO[:24]
# Liste vide pour tirage des dominos
DRAW=[]
SPLIT1=[]
SPLIT2=[]
#Fonction pour piocher et trier les 4 premiers dominos
def draw (list):   
    #efface les 4 dominos tirés
    del DRAW[0:4]
    for k in range (4):
        DRAW.append(list[k])
    del list[0:4]
    N = len(DRAW)
    for n in range(N):
        cle = DRAW[n]
        j = n-1
        while j>=0 and DRAW[j].number > cle.number:
            DRAW[j+1] = DRAW[j]
            j = j-1
        DRAW[j+1] = cle
    print(DRAW)
    return DRAW

def Split1(list,number):
    SPLIT1.append(list[number].land_one)
    SPLIT1.append(list[number].king_one)
    return SPLIT1

def Split2(list,number):
    SPLIT2.append(list[number].land_two)
    SPLIT2.append(list[number].king_two)
    return SPLIT2

def print_board(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            if (j % 2) == 0:
                if a[i][j] != 0:
                    print((DominoOne((a[i][j]), (a[i][j+1]))), end='')
                elif a[i][j] == 0:
                    print("    ", end='')
        print()