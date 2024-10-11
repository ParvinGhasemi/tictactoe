import numpy as np

ROWS = 3
COLUMNS = 3

def mark(row, column, player):
    board[row][column] = player

def is_valid_mark(row, column):
    return board[row][column] == 0

def is_board_full():
    for c in range(COLUMNS):
        for r in range(ROWS):
            if board[r][c] == 0:
                return False
    return True

board = np.zeros((ROWS,COLUMNS))

game_over = False
turn = 0

while not game_over:
    if turn % 2 == 0:
        row = int(input("Player 1: Enter the row number (0-2) :"))
        column = int(input("Player 1: Enter the column number (0-2) :"))
        if is_valid_mark(row, column):
            mark(row, column, 1)
        else:
            turn -= 1
    else:
        row = int(input1("Player 2: Enter the row number (0-2) :"))
        column = int(input("Player 2: Enter the column number (0-2) :"))
        if is_valid_mark(row, column):
            mark(row, column, 2)
        else:
            turn -= 1
    turn += 1