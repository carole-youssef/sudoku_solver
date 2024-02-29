#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GUI FOR SUDOKU GAME
"""

import pygame
import sudoku_solver

# initialize font
pygame.font.init()

# initialize colours
RED = (255,0,0)
BLACK = (0,0,0)
BLUE = (0,0,255)
WHITE = (255,255,255)

# initialize fonts to use
font1 = pygame.font.SysFont("comicsans", 40)
font2 = pygame.font.SysFont("comicsans", 20)

# size of window
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# display title
pygame.display.set_caption("SUDOKU GAME")

x = 0
y = 0
CELL_SIZE = WINDOW_WIDTH / 9
val = 0

# board for game
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# get coodrinates 
def get_cord(pos):
    global x
    x = pos[0] // CELL_SIZE * CELL_SIZE

    global y
    y = pos[1] // CELL_SIZE * CELL_SIZE

# function to draw required lines for making Sudoku grid
def draw():
    for i in range(9):
        for j in range(9):
            
            x = j * CELL_SIZE
            y = i * CELL_SIZE
            pygame.draw.rect(window, BLACK, (x, y, CELL_SIZE, CELL_SIZE), 1)

            # Draw the number if it exists
            if board[i][j] != 0:
                font = pygame.font.Font(None, 36)
                text = font.render(str(board[i][j]), True, BLUE)
                text_rect = text.get_rect(center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2))
                window.blit(text, text_rect)
                
    # draw bold vertical and horizontal lines to form grid
    for i in range(10):
        if i % 3 == 0 :
            line_width = 7
        else:
            line_width = 1
            
        pygame.draw.line(window, BLACK, (0, i * CELL_SIZE), (WINDOW_WIDTH, i * CELL_SIZE), line_width)
        pygame.draw.line(window, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, WINDOW_HEIGHT), line_width)

# function to fill value entered in cell by the user
def enter_value(val):
    text1 = font1.render(str(val), 1, BLUE)
    text_rect = text1.get_rect(center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2))
    window.blit(text1, text_rect)

# function to raise an error when a wrong value is entered
def raise_error1():
    text1 = font1.render("WRONG !!!", 1, RED)
    window.blit(text1, (20, 570))
    
def raise_error2():
    text1 = font1.render("Wrong !!! Not a valid Key", 1, (0, 0, 0))
    screen.blit(text1, (20, 570))

# check if value entered is valid
def valid_number():
    num = board[y // CELL_SIZE][x // CELL_SIZE]  # Get the number in the current cell
    pos = (y // CELL_SIZE, x // CELL_SIZE)  # Calculate the position of the current cell
    
    sudoku_solver.valid(board,num,pos)

# solve board
def solve_sudoku():
    sudoku_solver.solve(board)

    # make screen white
    window.fill(WHITE)

    # use the functions created above
    draw()
    
    pygame.display.update()
    pygame.time.delay(20)

# display the instructions of the game
def instruction():
    text1 = font2.render("PRESS D TO RESET TO DEFAULT / R TO EMPTY", 1, BLACK)
    text2 = font2.render("ENTER VALUES AND PRESS ENTER TO VISUALIZE", 1, BLACK)
    window.blit(text1, (20, 520))       
    window.blit(text2, (20, 540))

# display options when puzzle is solved
def result():
    text1 = font1.render("FINISHED PRESS R or D", 1, (0, 0, 0))
    window.blit(text1, (20, 570))

    
running = True
selected = None
flag1 = 0
flag2 = 0
rs = 0
error = 0

# game loop - main
while running:
    window.fill(WHITE)

    # looping through the events stored in events.get()
    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            running = False

        # get the mouse position to insert number
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            get_cord(pos)
            selected = (y,x)

        # get the number entered by user if key is pressed
        if event.type == pygame.KEYDOWN:   
            if event.key == pygame.K_1:
                val = 1
            if event.key == pygame.K_2:
                val = 2
            if event.key == pygame.K_3:
                val = 3
            if event.key == pygame.K_4:
                val = 4
            if event.key == pygame.K_5:
                val = 5
            if event.key == pygame.K_6:
                val = 6
            if event.key == pygame.K_7:
                val = 7
            if event.key == pygame.K_8:
                val = 8
            if event.key == pygame.K_9:
                val = 9

            # if an invalid number is entered, raise an error
            if event.key == pygame.K_RETURN:
                if board[int(y // CELL_SIZE)][int(x // CELL_SIZE)] == 0:
                    valid_number()
                    if sudoku_solver.valid(board, val, (int(y // CELL_SIZE), int(x // CELL_SIZE))):

                        board[int(y // CELL_SIZE)][int(x // CELL_SIZE)] = val
                        val = 0
                        flag1 = 0
                        
                    else:
                        # raise error
                        raise_error1()
                        pygame.time.delay(200)
                        val = 0
                        error = 1

            # if C is pressed, clear the sudoku board
            if event.key == pygame.K_c:
                flag2 = 0
                rs = 0
                error = 0
                board = [
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]

            # if D is pressed, resent the board to its default
            if event.key == pygame.K_d:
                flag2 = 0
                rs = 0
                error = 0
                board = [
                    [5, 3, 0, 0, 7, 0, 0, 0, 0],
                    [6, 0, 0, 1, 9, 5, 0, 0, 0],
                    [0, 9, 8, 0, 0, 0, 0, 6, 0],
                    [8, 0, 0, 0, 6, 0, 0, 0, 3],
                    [4, 0, 0, 8, 0, 3, 0, 0, 1],
                    [7, 0, 0, 0, 2, 0, 0, 0, 6],
                    [0, 6, 0, 0, 0, 0, 2, 8, 0],
                    [0, 0, 0, 4, 1, 9, 0, 0, 5],
                    [0, 0, 0, 0, 8, 0, 0, 7, 9]
                ]
                
    if selected is not None:
        row, col = selected

        x = col * CELL_SIZE
        y = row * CELL_SIZE
        pygame.draw.rect(window, RED, (x, y, CELL_SIZE, CELL_SIZE), 3)
                
    # if error encountered, raise error           
    if error == 1:
        raise_error2()
        error = 0

    # draw board   
    draw()
        
    # display instructions and options
    instruction()

    # draw the value entered by user
    if val != 0:
        enter_value(val)

    # update the display
    pygame.display.update() 
 
                      
# quit game
pygame.quit()









