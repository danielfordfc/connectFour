import sys
import time

import numpy as np
import pygame


def create_board():
    ROW_COUNT = int(input("Select number of rows for game to have:"))
    COL_COUNT = int(input("Select number of columns for game to have:"))
    board_new = np.zeros((ROW_COUNT, COL_COUNT))
    return board_new, ROW_COUNT, COL_COUNT


# Initialise Board
board, ROW_COUNT, COL_COUNT = create_board()
ROW_COUNT_INDEX = ROW_COUNT - 1
COL_COUNT_INDEX = COL_COUNT - 1
game_over = False
turn = 1


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[0][col] == 0


def get_next_open_row(board, col):
    # Finds next open row in the matrix
    # Array matrices reference 0,0 top left, x,x bottom right
    # will iterate from 0 to row_count -1
    for r in range(ROW_COUNT):
        if board[ROW_COUNT_INDEX - r][col] == 0:
            return ROW_COUNT_INDEX - r


def winning_move(board, p):
    # horizontals to determine a win - 0,1,2,3 - right 3 from that
    for c in range(COL_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == p and board[r][c + 1] == p and board[r][c + 2] == p and board[r][c + 3] == p:
                return True

    # Vertical for win
    for r in range(ROW_COUNT - 3):
        for c in range(COL_COUNT):
            if board[r][c] == p and board[r + 1][c] == p and board[r + 2][c] == p and board[r + 3][c] == p:
                return True

    # Diagonal down win
    for c in range(COL_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == p and board[r + 1][c + 1] == p and board[r + 2][c + 2] == p and board[r + 3][c + 3] == p:
                return True

    # Diagonal up win
    for c in range(COL_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == p and board[r - 1][c + 1] == p and board[r - 2][c + 2] == p and board[r - 3][c + 3] == p:
                return True


def draw_board(board):
    # print(board)
    # initially draw blue rectangle with black circle inside
    for c in range(COL_COUNT):
        for r in range(ROW_COUNT):
            # rectangle requires, width, height, x and y pos
            pygame.draw.rect(screen, BLUE,
                             (c * SQUARE_SIZE, (r * SQUARE_SIZE) + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            if board[r][c] == 0:
                pygame.draw.circle(screen, BLACK, (
                    int(c * SQUARE_SIZE + (0.5 * SQUARE_SIZE)), int((r * SQUARE_SIZE) + int((1.5 * SQUARE_SIZE)))),
                                   int(SQUARE_SIZE * 0.4))
            elif board[r][c] == 1:
                pygame.draw.circle(screen, RED, (
                    int(c * SQUARE_SIZE + (0.5 * SQUARE_SIZE)), int((r * SQUARE_SIZE) + int((1.5 * SQUARE_SIZE)))),
                                   int(SQUARE_SIZE * 0.4))
            elif board[r][c] == 2:
                print(str(board[r][c]))
                pygame.draw.circle(screen, GREEN, (
                    int(c * SQUARE_SIZE + (0.5 * SQUARE_SIZE)), int((r * SQUARE_SIZE) + int((1.5 * SQUARE_SIZE)))),
                                   int(SQUARE_SIZE * 0.4))


# Initialize Pygame and set params
pygame.init()

# Define Colours to be used
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Define Dimensions of board that dynamically scale on user declared sizing.
SQUARE_SIZE = 100
WIDTH = COL_COUNT * SQUARE_SIZE
HEIGHT = (ROW_COUNT + 1) * SQUARE_SIZE
SIZE = (WIDTH, HEIGHT)

# Draw the initial board and invoke draw_board. Always make sure to update the display? Seems to be needed.
screen = pygame.display.set_mode(SIZE)
draw_board(board)
pygame.display.update()

# Main Game Loop
while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Calculate x position of click
            # selection = int(round((event.pos[0] / 100) -((event.pos[0] % 100) / 100), 1))

            # # Ask for Player 1 input
            if turn % 2 == 1:
                print("Player 1 make your selection! 0 - " + str(COL_COUNT_INDEX) + ":")
                col = int(round((event.pos[0] / 100) - ((event.pos[0] % 100) / 100), 1))
                while col >= COL_COUNT:
                    print("Selection outside of range!")
                    print("Player 1 make your selection! 0 - " + str(COL_COUNT_INDEX) + ":")
                    col = int(round((event.pos[0] / 100) - ((event.pos[0] % 100) / 100), 1))

                if is_valid_location(board, col):
                    row_to_plop = get_next_open_row(board, col)
                    drop_piece(board, row_to_plop, col, 1)

                if winning_move(board, 1):
                    for i in range(15):
                        print("PLAYER 1 WINS!!")
                        time.sleep(0.1)

                    game_over = True

                draw_board(board)
                pygame.display.update()

            # Ask for Player 2 input
            else:
                print("Player 2 make your selection! 0 - " + str(COL_COUNT_INDEX) + ":")
                col = int(round((event.pos[0] / 100) - ((event.pos[0] % 100) / 100), 1))
                while col >= COL_COUNT:
                    print("Selection outside of range!")
                    print("Player 2 make your selection! 0 - " + str(COL_COUNT_INDEX) + ":")
                    col = int(round((event.pos[0] / 100) - ((event.pos[0] % 100) / 100), 1))

                if is_valid_location(board, col):
                    row_to_plop = get_next_open_row(board, col)
                    drop_piece(board, row_to_plop, col, 2)

                if winning_move(board, 2):
                    for i in range(15):
                        print("PLAYER 2 WINS!!")
                        time.sleep(0.1)
                    game_over = True

                draw_board(board)
                pygame.display.update()

            # Increment turn counter
            turn += 1
            print("turn = " + str(turn))

input("Press any key to Exit!")
