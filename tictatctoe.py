import numpy as np

ROWS = 3
COLUMNS = 3

def mark(row, column, player):
    board[row][column] = player

board = np.zeros((ROWS,COLUMNS))

print(board)
mark(1,0,2)
print(board)