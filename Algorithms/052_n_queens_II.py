#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def __init__(self):
        self.solutions = 0
        
    # @return a list of lists of string
    def totalNQueens(self, n):
        board = [[False] * n for i in range(n)]

        self.solve(board, 0)
        
        return self.solutions
    
    def solve(self, board, column):
        if column == len(board):
            self.solutions += 1
            return

        for i in range(len(board)):
            if self.is_valid(board, i, column):
                board[i][column] = True
                self.solve(board, column + 1)
                board[i][column] = False
    
    def is_valid(self, board, row, column):
        for i in range(column):
            if board[row][i]:
                return False
        
        i, j = row, column
        
        while i >= 0 and j >= 0:
            if board[i][j]:
                return False
            
            i -= 1
            j -= 1
        
        i, j = row, column
        
        while i < len(board) and j >= 0:
            if board[i][j]:
                return False
            
            i += 1
            j -= 1
        
        return True
