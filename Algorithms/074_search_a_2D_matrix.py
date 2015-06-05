#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        row = len(matrix)
        column = len(matrix[0])
        
        low = 0
        high = row - 1
        
        while low <= high:
            mid = (low + high) / 2
            mid_value = matrix[mid][0]

            if mid_value == target:
                return True
            elif mid_value < target and low + 1 <= row - 1 and matrix[low + 1][0] <= target:
                low += 1
            elif mid_value > target and high - 1 >= 0 and matrix[high - 1][0] >= target:
                high -= 1
            else:
                break
        
        target_row = mid

        if mid_value < target:
            low = 0
            high = column - 1
            
            while low <= high:
                mid = (low + high) / 2
                mid_value = matrix[target_row][mid]
                
                if mid_value == target:
                    return True
                elif mid_value < target:
                    low += 1
                else:
                    high -= 1
        
        return False
