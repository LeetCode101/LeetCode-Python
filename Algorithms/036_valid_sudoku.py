#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        digits = []
        
        # Row
        for i in range(9):
            digits = []
            
            for j in range(9):
                cell = board[i][j]
                
                if cell == '.':
                    continue
                
                if cell in digits:
                    return False
                else:
                    digits.append(cell)
        
        # Column
        for i in range(9):
            digits = []
            
            for j in range(9):
                cell = board[j][i]
                
                if cell == '.':
                    continue
                
                if cell in digits:
                    return False
                else:
                    digits.append(cell)
        
        # Sub-grid
        for i in range(3):
            for j in range(3):
                digits = []
                
                for m in range(3 * i, 3 * i + 3):
                    for n in range(3 * j, 3 * j + 3):
                        cell = board[m][n]
                        
                        if cell == '.':
                            continue
                        
                        if cell in digits:
                            return False
                        else:
                            digits.append(cell)
        
        return True
