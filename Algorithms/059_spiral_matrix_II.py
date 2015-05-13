#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        m = 1
        matrix = [[1] * n for i in range(n)]
        
        for i in range(n / 2):
            for j in range(i, n - 1 - i):
                matrix[i][j] = m
                m += 1
            
            for j in range(i, n - 1 - i):
                matrix[j][n - 1 - i] = m
                m += 1
            
            for j in range(n - 1 - i, i, -1):
                matrix[n - 1 - i][j] = m
                m += 1
            
            for j in range(n - 1 - i, i, -1):
                matrix[j][i] = m
                m += 1
        
        if n & 1 == 1:
            matrix[n / 2][n / 2] = m
        
        return matrix
