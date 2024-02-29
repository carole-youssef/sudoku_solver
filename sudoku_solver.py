#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
python sudoku solver using backtracking

Carole Youssef
"""

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

# solving the board - using recursion
def solve(bo):
    # base case of recursion - once we reach it were done
    find  = find_empty(bo)
    if not find:
        return True # meaning we found the solution
    else:
        row,col = find # empty position
        
    for i in range(1,10): # looping through nums 1 - 9
        if valid(bo, i, (row, col)): # if valid, plug that value in the board
            bo[row][col] = i
            
            if solve(bo): # recursion - keep trying for each value
                return True
            
            bo[row][col] = 0

# if no numbers work in this position it returns false
# and back tracks to an empty position 0 - resetting it
# tries again with a diff value until a solution is found
    return False
    

# finding if the current board is valid
# depending on the number we input and its position
# checking row, column and "square" we are in 
def valid(bo, num , pos):
    
    # check row
    for i in range(len(bo[0])):
        # checking each elemnt in row to see if is equal to num
        # if its the position we just inserted, we ignore that pos
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    
    #check column 
    for i in range(len(bo)):
        # same as above but going down
        #check if column value is = to same num we insterted
        # and make sure its not the exat pos that we inserted smthn into
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    
    # check box
    # making the coordinates of each box
    box_x = pos[1] // 3 
    box_y = pos[0] // 3
    
    # looping through each small square
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
            
    return True

# printing the board - visual purposes
# using the board we made using random above
def print_board(bo):
    
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print ("- - - - - - - - - - - - ")
        
        for j in range(len(bo[0])):
            if j % 3 == 0 and j!=0:
                print (" | ", end = "") # doesnt print \n, goes to next line
                
            if j == 8:
                print(bo[i][j])
                
            else:
                print(str(bo[i][j])+ " ", end  = "")
                
        
# given a board, find an empty square and returns its position
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j) # row, column
    return None

#print_board(board)
solve(board)
print("------------------------")
#print_board(board)
