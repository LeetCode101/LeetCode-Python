#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        row = len(matrix)
        column = len(matrix[0])
        is_first_row_zero = False
        is_first_column_zero = False
        
        for i in range(column):
            if matrix[0][i] == 0:
                is_first_row_zero = True
                break
        
        for i in range(row):
            if matrix[i][0] == 0:
                is_first_column_zero = True
                break
        
        for i in range(1, row):
            for j in range(1, column):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, row):
            for j in range(1, column):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] =0
        
        if is_first_row_zero:
            for i in range(column):
                matrix[0][i] = 0
        
        if is_first_column_zero:
            for i in range(row):
                matrix[i][0] = 0
