#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        self.solve(board)
    
    def solve(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for k in range(1, 10):
                        board[i][j] = str(k)
                        
                        if self.is_valid(board, i, j) and self.solve(board):
                            return True
                        
                        board[i][j] = '.'
                    
                    return False
        
        return True
    
    def is_valid(self, board, row, column):
        # Check row
        for i in range(9):
            if i != row and board[i][column] == board[row][column]:
                return False
        
        # Check column
        for j in range(9):
            if j != column and board[row][j] == board[row][column]:
                return False
        
        # Check sub-grid
        for i in range(row / 3 * 3, 3 * (row / 3 + 1)):
            for j in range(column / 3 * 3, 3 * (column / 3 + 1)):
                if i != row and j != column and board[i][j] == board[row][column]:
                    return False
        
        return True
