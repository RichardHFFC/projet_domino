import random
from colors import bcolors

# Définition de joueurs
PLAYER_ONE = 1
PLAYER_TWO = 2

# Class Castle pour définir les chateaux des joueurs
class Castle :
    def __init__(self, number, player):
        self.number = number
        self.player = player

    def __str__(self):
        if self.player == 1 :
            player = f"{bcolors.BWHITEB}C_P1"+f"{bcolors.BASE}"
        elif self.player == 2:
            player = f"{bcolors.BWHITEB}C_P2"+f"{bcolors.BASE}"

        return "%2s | %s |" % (self.number, player)
KING = [
    Castle(1,PLAYER_ONE),
    Castle(2,PLAYER_ONE),
    Castle(3,PLAYER_TWO),
    Castle(4,PLAYER_TWO)
    ]