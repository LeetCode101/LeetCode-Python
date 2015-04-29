#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        solutions = []
        board = [[False] * n for i in range(n)]

        self.solve(board, 0, solutions)
        
        return solutions
    
    def solve(self, board, column, solutions):
        if column == len(board):
            self.set_queens(board, solutions)
            return

        for i in range(len(board)):
            if self.is_valid(board, i, column):
                board[i][column] = True
                self.solve(board, column + 1, solutions)
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
    
    def set_queens(self, board, solutions):
        solution = []

        for i in range(len(board)):
            solution.append(''.join(['Q' if board[i][j] else '.' for j in range(len(board))]))
        
        solutions.append(solution)
