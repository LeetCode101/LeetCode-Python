#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        paths = [[0] * n for i in range(m)]
        
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                break
            
            paths[0][i] = 1
        
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            
            paths[i][0] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    paths[i][j] = paths[i - 1][j] + paths[i][j - 1]
        
        return paths[m - 1][n - 1]
