#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, word):
        row = len(board)
        column = len(board[0])
        visited = [[False] * column for i in range(row)]
        
        for i in range(row):
            for j in range(column):
                if self.search(board, visited, i, j, row, column, word, 0):
                    return True
        
        return False
    
    def search(self, board, visited, current_row, current_column, max_row, max_column, word, index):
        if index == len(word):
            return True
        
        if current_row < 0 or current_column < 0 or current_row >= max_row or current_column >= max_column:
            return False
        
        if visited[current_row][current_column] or board[current_row][current_column] != word[index]:
            return False
            
        visited[current_row][current_column] = True
        
        if self.search(board, visited, current_row - 1, current_column, max_row, max_column, word, index + 1):
            return True
        
        if self.search(board, visited, current_row + 1, current_column, max_row, max_column, word, index + 1):
            return True
        
        if self.search(board, visited, current_row, current_column - 1, max_row, max_column, word, index + 1):
            return True
        
        if self.search(board, visited, current_row, current_column + 1, max_row, max_column, word, index + 1):
            return True
        
        visited[current_row][current_column] = False
        
        return False
