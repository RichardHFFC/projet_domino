from fctdomino import print_board

class Player :
    def __init__(self, player):
        self.player = player
        self.a = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]]
        self.b = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]]  
    

    
    def __str__(self):
        if self.player == 1 :
            return "Player One\n" + "Board A\n" + print_board(self.a)+"\nBoard B\n" + print_board(self.b)

        if self.player == 2:
            return "Player One\n" + "Board A\n" + print_board(self.a)+"\nBoard B\n" + print_board(self.b)
def Castle(line,colum,board):
    if (colum == 1): 
        colum = colum -1
    elif(colum == 2): 
        colum = colum + 0
    elif(colum == 3): 
        colum = colum + 1
    elif(colum == 4): 
        colum = colum + 2 
    elif(colum == 5): 
        colum = colum + 3
    board[(line-1)][colum]=7   

def Dom(line,colum,board,Dom):
    while True :
        if (colum == 1): 
            colum = colum -1
        elif(colum == 2): 
            colum = colum + 0
        elif(colum == 3): 
            colum = colum + 1
        elif(colum == 4): 
            colum = colum + 2 
        elif(colum == 5): 
            colum = colum + 3
        if board[line-1][colum]==0:
            board[(line-1)][colum]=Dom[0]
            board[(line-1)][colum+1]=Dom[1]
            break
        elif board[line-1][colum] !=0 :  
            print("choose another case") 
            while True:
                line = int(input("what is your line (1,2,3,4,5) : "))
                if ((line == 1)or(line == 2)or(line == 3)or(line == 4)or(line == 5)):
                    break
            while True:
                colum = int(input("what is your column (1,2,3,4,5) : "))
                if ((colum == 1)or(colum == 2)or(colum == 3)or(colum == 4)or(colum == 5)):
                    break