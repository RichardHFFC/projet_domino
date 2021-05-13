import random
from colors import bcolors

# Définition des types de terrain
CASTLE = 0
WHEAT = 1
FOREST = 2
WATER = 3
SHEEP = 4
WASTELAND = 5
CAVE = 6
# Définition de joueurs
PLAYER_ONE = 10
PLAYER_TWO = 20

# class Domino pour définir un domino
class Domino:
    def __init__(self, number, land_one, king_one, land_two, king_two):
        self.number = number
        self.land_one = land_one
        self.king_one = king_one
        self.land_two = land_two
        self.king_two = king_two

    def __str__(self):
        if self.king_one == 3:
            kingOne = "***"
        elif self.king_one == 2:
            kingOne = "** "
        elif self.king_one == 1:
            kingOne = "*  "
        elif self.king_one == 0:
            kingOne = "   "
        if self.king_one == 3:
            kingOne = "***"
        elif self.king_one == 2:
            kingOne = "** "
        elif self.king_one == 1:
            kingOne = "*  "
        elif self.king_one == 0:
            kingOne = "   " 

        if self.land_one == 6:
            landOne = f"{bcolors.BBLACKB}C" + kingOne + f"{bcolors.BASE}"
        elif self.land_one == 5:
            landOne = f"{bcolors.BREDB}W" + kingOne + f"{bcolors.BASE}"
        elif self.land_one == 4:
            landOne = f"{bcolors.BPURPLEB}S" + kingOne + f"{bcolors.BASE}"
        elif self.land_one == 3:
            landOne = f"{bcolors.BBLUEB}W" + kingOne + f"{bcolors.BASE}"
        elif self.land_one == 2:
            landOne = f"{bcolors.BGREENB}F" + kingOne + f"{bcolors.BASE}"
        elif self.land_one == 1:
            landOne = f"{bcolors.BYELLOWB}W" + kingOne + f"{bcolors.BASE}"

        if self.king_two == 3:
            kingTwo = "***"
        elif self.king_two == 2:
            kingTwo = "** "
        elif self.king_two == 1:
            kingTwo = "*  "
        elif self.king_two == 0:
            kingTwo = "   "
        if self.king_two == 3:
            kingTwo = "***"
        elif self.king_two == 2:
            kingTwo = "** "
        elif self.king_two == 1:
            kingTwo = "*  "
        elif self.king_two == 0:
            kingTwo = "   " 

        if self.land_two == 6:
            landTwo = f"{bcolors.BBLACKB}C" + kingTwo + f"{bcolors.BASE}"
        elif self.land_two == 5:
            landTwo = f"{bcolors.BREDB}W" + kingTwo + f"{bcolors.BASE}"
        elif self.land_two == 4:
            landTwo = f"{bcolors.BPURPLEB}S" + kingTwo + f"{bcolors.BASE}"
        elif self.land_two == 3:
            landTwo = f"{bcolors.BBLUEB}W" + kingTwo + f"{bcolors.BASE}"
        elif self.land_two == 2:
            landTwo = f"{bcolors.BGREENB}F" + kingTwo + f"{bcolors.BASE}"
        elif self.land_two == 1:
            landTwo = f"{bcolors.BYELLOWB}W" + kingTwo + f"{bcolors.BASE}"
           
        return "%2s | %s | %s | " % (self.number, landOne, landTwo)
    
# Class castle pour définir les chateaux des joueurs
class Castle :
    def __init__(self, number, player):
        self.number = number
        self.player = player

    def __str__(self):
        if self.player == 10 :
            player = f"{bcolors.BWHITEB}C_P1"+f"{bcolors.BASE}"
        elif self.player == 20:
            player = f"{bcolors.BWHITEB}C_P2"+f"{bcolors.BASE}"

        return "%2s | %s |" % (self.number, player)
# Class pour tirer 4 quarte

#Création de la liste des chateaux 
KING = [
    Castle(1,PLAYER_ONE),
    Castle(2,PLAYER_ONE),
    Castle(3,PLAYER_TWO),
    Castle(4,PLAYER_TWO)
    ]
# création de la liste des 48 dominos
DOMINO = [
    Domino(1, WHEAT, 0, WHEAT, 0),
    Domino(2, WHEAT, 0, WHEAT, 0),
    Domino(3, FOREST, 0, FOREST, 0),
    Domino(4, FOREST, 0, FOREST, 0),
    Domino(5, FOREST, 0, FOREST, 0),
    Domino(6, FOREST, 0, FOREST, 0),
    Domino(7, WATER, 0, WATER, 0),
    Domino(8, WATER, 0, WATER, 0),
    Domino(9, WATER, 0, WATER, 0),
    Domino(10, SHEEP, 0, SHEEP, 0),
    Domino(11, SHEEP, 0, SHEEP, 0),
    Domino(12, WASTELAND, 0, WASTELAND, 0),
    Domino(13, WHEAT, 0, FOREST, 0),
    Domino(14, WHEAT, 0, WATER, 0),
    Domino(15, WHEAT, 0, SHEEP, 0),
    Domino(16, WHEAT, 0, WASTELAND, 0),
    Domino(17, FOREST, 0, WATER, 0),
    Domino(18, FOREST, 0, SHEEP, 0),
    Domino(19, WHEAT, 1, FOREST, 0),
    Domino(20, WHEAT, 1, WATER, 0),
    Domino(21, WHEAT, 1, SHEEP, 0),
    Domino(22, WHEAT, 1, WASTELAND, 0),
    Domino(23, WHEAT, 1, CAVE, 0),
    Domino(24, FOREST, 1, WHEAT, 0),
    Domino(25, FOREST, 1, WHEAT, 0),
    Domino(26, FOREST, 1, WHEAT, 0),
    Domino(27, FOREST, 1, WHEAT, 0),
    Domino(28, FOREST, 1, WATER, 0),
    Domino(29, FOREST, 1, SHEEP, 0),
    Domino(30, WATER, 1, WHEAT, 0),
    Domino(31, WATER, 1, WHEAT, 0),
    Domino(32, WATER, 1, FOREST, 0),
    Domino(33, WATER, 1, FOREST, 0),
    Domino(34, WATER, 1, FOREST, 0),
    Domino(35, WATER, 1, FOREST, 0),
    Domino(36, WHEAT, 0, SHEEP, 1),
    Domino(37, WATER, 0, SHEEP, 1),
    Domino(38, WHEAT, 0, WASTELAND, 1),
    Domino(39, SHEEP, 0, WASTELAND, 1),
    Domino(40, CAVE, 1, WHEAT, 0),
    Domino(41, WHEAT, 0, SHEEP, 2),
    Domino(42, WATER, 0, SHEEP, 2),
    Domino(43, WHEAT, 0, WASTELAND, 2),
    Domino(44, SHEEP, 0, WASTELAND, 2),
    Domino(45, CAVE, 2, WHEAT, 0),
    Domino(46, WASTELAND, 0, CAVE, 2),
    Domino(47, WASTELAND, 0, CAVE, 2),
    Domino(48, WHEAT, 0, CAVE, 3)
]
# liste vide pour tirage de 4 dominos
DRAW =[]
# Mélange de la liste 
random.shuffle(DOMINO)
# Sélection des 24 premiers dominos de la liste mélangée
DOMINO_LIST = DOMINO[:24]
#Fonction pour piocher les 4 premier dominos
def draw (list):
    for k in range (4):
        DRAW.append(list[k])
    del list[0:4]
    return DRAW
#Fonction du tri de la liste de dominos piochés 
def sort_insertion(list):
    N = len(list)
    for n in range(N):
        cle = list[n]
        j = n-1
        while j>=0 and list[j].number > cle.number:
            list[j+1] = list[j]
            j = j-1
        list[j+1] = cle
    return list





# Test du programme    
print(f"{bcolors.GREEN}*************************************")
print("*  Affichage liste mélangée de 24 Dominos   *")
print(f"*************************************{bcolors.BASE}")

for k in range(len(DOMINO_LIST)):
    print(DOMINO_LIST[k])

print(" ")
print(f"taille liste : {len(DOMINO_LIST)}")
print(" ")

print(f"{bcolors.GREEN}***********************************")
print("*    Fin liste mélangée de 24 Dominos    *")
print(f"***********************************{bcolors.BASE}")

# boucle pour faire 6 tirages 
for i in range(6):
    #pioche des 4 premiers dominos
    draw(DOMINO_LIST)

    print(f"{bcolors.GREEN}*************************************")
    print("*  Affichage du tirage de 4 dominos   *")
    print(f"*************************************{bcolors.BASE}")

    for k in range(len(DRAW)):
        print(DRAW[k])

    print(" ")
    print(f"taille liste : {len(DRAW)}")
    print(" ")

    print(f"{bcolors.GREEN}***********************************")
    print("*    Fin du tirage de 4 dominos   *")
    print(f"***********************************{bcolors.BASE}")

    # tri des 4 dominos piochés
    DRAW = sort_insertion(DRAW)

    print(f"{bcolors.GREEN}*************************************")
    print("*  Affichage du tirage de 4 dominos triés  *")
    print(f"*************************************{bcolors.BASE}")

    for k in range(len(DRAW)):
        print(DRAW[k])

    print(" ")
    print(f"taille liste : {len(DRAW)}")
    print(" ")

    #efface les 4 dominos tirés
    del DRAW[0:4]

    print(f"{bcolors.GREEN}***********************************")
    print("*    Fin du tirage de 4 dominos triés  *")
    print(f"***********************************{bcolors.BASE}")

    print(f"{bcolors.GREEN}*************************************")
    print("*  Affichage des dominos qui restent dans la pioche   *")
    print(f"*************************************{bcolors.BASE}")

    for k in range(len(DOMINO_LIST)):
        print(DOMINO_LIST[k])

    print(" ")
    print(f"taille liste : {len(DOMINO_LIST)}")
    print(" ")

    print(f"{bcolors.GREEN}***********************************")
    print("*    Fin des dominos qui restent dans la pioche  *")
    print(f"***********************************{bcolors.BASE}")