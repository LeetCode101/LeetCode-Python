#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        paths = [[0] * n for i in range(m)]
        paths[0] = [1] * n
        
        for i in range(m):
            paths[i][0] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                paths[i][j] = paths[i - 1][j] + paths[i][j - 1]
        
        return paths[m - 1][n - 1]
