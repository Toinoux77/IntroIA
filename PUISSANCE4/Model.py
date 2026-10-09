#Puissance4

WIDTH = 7
HEIGHT = 6

def new_board():
    return [[0 in range(WIDTH)] in range(HEIGHT)]

def is_win(board):
    count1 = 0
    count2 = 0
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if board[i][j] == 1:
                

