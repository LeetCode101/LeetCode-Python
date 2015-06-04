#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        row = len(matrix)
        column = len(matrix[0])
        is_original_zero = [[False] * column for i in range(row)]
        
        for i in range(row):
            for j in range(column):
                is_original_zero[i][j] = matrix[i][j] == 0

        i = 0
        j = 0
        
        for i in range(row):
            for j in range(column):
                if matrix[i][j] == 0 and is_original_zero[i][j]:
                    for m in range(column):
                        matrix[i][m] = 0
                    
                    for n in range(row):
                        matrix[n][j] = 0
