import numpy as np

ROWS = 3
COLUMNS = 3

def mark(row, column, player):
    board[row][column] = player


def is_valid_mark(row, column):
    return board[row][column] == 0


def is_this_a_winnig_move(player):
    if player == 1:
        message = "Player 1 Won The Game!"
    else:
        message = "Player 2 Won The Game!"

    for r in range(ROWS):
        if board[r][0] == player and board[r][1] == player and board[r][2] == player:
            print(message)
            return True
    for c in range(COLUMNS):
        if board[0][c] == player and board[1][c] == player and board[2][c] == player:
            print(message)
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        print(message)
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        print(message)
        return True


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
        # Player 1
        row = int(input("Player 1: Enter the row number (0-2) :"))
        column = int(input("Player 1: Enter the column number (0-2) :"))
        if is_valid_mark(row, column):
            mark(row, column, 1)
            if is_this_a_winnig_move(1):
                game_over = True
        else:
            turn -= 1
    else:
        # Player 2
        row = int(input("Player 2: Enter the row number (0-2) :"))
        column = int(input("Player 2: Enter the column number (0-2) :"))
        if is_valid_mark(row, column):
            mark(row, column, 2)
            if is_this_a_winnig_move(2):
                game_over = True
        else:
            turn -= 1
    turn += 1
    print(board)
    if game_over == True:
        print("Game Over")
