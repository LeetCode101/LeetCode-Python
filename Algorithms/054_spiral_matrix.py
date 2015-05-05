#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        row = len(matrix)
        
        if row == 0:
            return []
            
        column = len(matrix[0])
        spiral_matrix = []
        
        for i in range(int(math.ceil(min(row, column) / 2.0))):
            if i == row - 1 - i:
                spiral_matrix += matrix[i][i:column - i]
            elif i == column - 1 - i:
                spiral_matrix += [matrix[j][i] for j in range(i, row - i)]
            else:
                spiral_matrix += [matrix[i][j] for j in range(i, column - 1 - i)]
                spiral_matrix += [matrix[j][column - 1 - i] for j in range(i, row - 1 - i)]
                spiral_matrix += [matrix[row - 1 - i][j] for j in range(column - 1 - i, i, -1)]
                spiral_matrix += [matrix[j][i] for j in range(row - 1 - i, i, -1)]
        
        return spiral_matrix
