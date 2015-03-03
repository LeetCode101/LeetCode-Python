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
    
    def is_valid(self, board, x, y):
        # Check row
        for i in range(9):
            if i != x and board[i][y] == board[x][y]:
                return False
        
        # Check column
        for j in range(9):
            if j != y and board[x][j] == board[x][y]:
                return False
        
        # Check sub-grid
        start_x = x / 3
        start_y = y / 3
        
        for i in range(start_x * 3, 3 * start_x + 3):
            for j in range(start_y * 3, 3 * start_y + 3):
                if i != x and j != y and board[i][j] == board[x][y]:
                    return False
        
        return True
