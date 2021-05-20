from numpy.lib.index_tricks import AxisConcatenator
from colors import bcolors
import numpy as np
BOARD =[]
LAND = np.zeros((1,2))
CROWN = np.zeros((1,2))

class Board :
    def __init__(objet) :
        global LAND
        global CROWN
        for i in range (12) :
            LAND = np.append(LAND,np.zeros((1,2)),axis = 0)
        LAND = LAND.reshape(5,10)
        for i in range (12) :
            CROWN = np.append(CROWN,np.zeros((1,2)),axis = 0)
        CROWN = CROWN.reshape(5,10)
        return LAND,CROWN

print(BOARD)
for i in range(50):
    BOARD = np.append(BOARD,np.zeros((1)),axis = 0)
#BOARD1 = np.resize(BOARD,new_shape=((1,5,2)))
print("")
print(BOARD)
print("")
print(BOARD.shape)
print("")
BOARD = BOARD.reshape(5,10)
print(BOARD.shape)
print("")
print(BOARD)
print("")
BOARD[0,0] = 2
BOARD[4,3] = 5
print(BOARD)
