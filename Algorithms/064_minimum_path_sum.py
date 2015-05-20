#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        
        sums = [[0] * n for i in range(m)]
        sums[0][0] = grid[0][0]
        
        for i in range(1, n):
            sums[0][i] = sums[0][i - 1] + grid[0][i]
        
        for i in range(1, m):
            sums[i][0] = sums[i - 1][0] + grid[i][0]
        
        for i in range(1, m):
            for j in range(1, n):
                sums[i][j] = min(sums[i - 1][j], sums[i][j - 1]) + grid[i][j]
        
        return sums[m - 1][n - 1]
