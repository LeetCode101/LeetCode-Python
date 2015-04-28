#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param matrix, a list of lists of integers
    # @return nothing (void), do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        n = len(matrix)
        
        for i in range(n / 2):
            for j in range(i, n - 1 - i):
                self.swap(matrix, i, j, j, n - 1 - i)
                self.swap(matrix, i, j, n - 1 - i, n - 1 - j)
                self.swap(matrix, i, j, n - 1 - j, i)
                
    def swap(self, matrix, i1, j1, i2, j2):
        matrix[i1][j1], matrix[i2][j2] = matrix[i2][j2], matrix[i1][j1]
