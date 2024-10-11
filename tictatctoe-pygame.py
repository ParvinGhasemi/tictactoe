import numpy as np
import pygame
import math

ROWS = 3
COLUMNS = 3

WIDTH = 600
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

CIRCLE = pygame.image.load('images/circle.png')
CROSS = pygame.image.load('images/cross.png')
CIRCLE = pygame.transform.scale(CIRCLE, (100, 100))  # Resize circle
CROSS = pygame.transform.scale(CROSS, (100, 100))    # Resize cross

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


def draw_board():
    for c in range(COLUMNS):
        for r in range(ROWS):
            if board[r][c] == 1:
                window.blit(CIRCLE, (c * 200 + 50, r * 200 + 50))
            elif board[r][c] == 2:
                window.blit(CROSS, (c * 200 + 50, r * 200 + 50))
    pygame.display.update()  


def draw_line():
    pygame.draw.line(window, BLACK, (200, 0), (200, 600), 5)
    pygame.draw.line(window, BLACK, (400, 0), (400, 600), 5)
    pygame.draw.line(window, BLACK, (0, 200), (600, 200), 5)
    pygame.draw.line(window, BLACK, (0, 400), (600, 400), 5)



def is_this_a_winning_move(player):
    if player == 1:
        winning_color = BLUE
        message = "Player 1 Won The Game!"
    else:
        winning_color = RED
        message = "Player 2 Won The Game!"

    for r in range(ROWS):
        if board[r][0] == player and board[r][1] == player and board[r][2] == player:
            pygame.draw.line(window, winning_color, (10, r*200 + 100), (WIDTH-10, r*200 + 100), 10)
            print(message)
            return True
    for c in range(COLUMNS):
        if board[0][c] == player and board[1][c] == player and board[2][c] == player:
            pygame.draw.line(window, winning_color, (c*200 + 100, 10), (c*200 + 100, HEIGHT-10), 10)
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        pygame.draw.line(window, winning_color, (10, 10), (WIDTH-10, HEIGHT-10), 10)
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        pygame.draw.line(window, winning_color, (10, HEIGHT-10), (WIDTH-10, 10), 10)
        return True




board = np.zeros((ROWS,COLUMNS))

game_over = False
turn = 0

pygame.init()
window = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Tic Tac Toe")
window.fill(WHITE)
draw_line()
pygame.display.update()


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            row = math.floor(event.pos[1]/200)
            column = math.floor(event.pos[0]/200)

            if turn % 2 == 0:
                # Player 1

                if is_valid_mark(row, column):
                    mark(row, column, 1)
                    if is_this_a_winning_move(1):
                        game_over = True
                else:
                    turn -= 1
            else:
                # Player 2
                if is_valid_mark(row, column):
                    mark(row, column, 2)
                    if is_this_a_winning_move(2):
                        game_over = True
                else:
                    turn -= 1
            turn += 1
            print(board)
            draw_board()

            if is_board_full():
                game_over = True
            if game_over == True:
                print("Game Over")
                pygame.time.wait(2000)
                board.fill(0)
                window.fill(WHITE)
                draw_line()
                draw_board()
                game_over = False
                pygame.display.update()

pygame.quit()