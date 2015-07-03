#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalRectangle(self, matrix):
        if len(matrix) == 0:
            return 0
        
        max_area = 0
        row = len(matrix)
        column = len(matrix[0])
        
        for i in range(row):
            histogram = self.create_histogram(i, column, matrix)
            
            max_area = max(max_area, self.largest_rectangle_area(histogram))
        
        return max_area
    
    def largest_rectangle_area(self, height):
        max_area = 0
        height = height + [0]
        length = len(height)
        index_of_increasing_bar = []
        
        for i in range(length):
            while len(index_of_increasing_bar) != 0 and height[i] < height[index_of_increasing_bar[-1]]:
                h = height[index_of_increasing_bar.pop()]
                
                if len(index_of_increasing_bar) == 0:
                    max_area = max(max_area, i * h)
                else:
                    max_area = max(max_area, (i - index_of_increasing_bar[-1] - 1) * h)
            
            index_of_increasing_bar.append(i)
        
        return max_area
    
    def create_histogram(self, current_row, max_column, matrix):
        histogram = []
        
        for j in range(max_column):
            if matrix[current_row][j] == '1':
                height = 1
                
                for k in range(current_row - 1, -1, -1):
                    if matrix[k][j] == '1':
                        height += 1
                    else:
                        break
                
                histogram.append(height)
            else:
                histogram.append(0)
        
        return histogram
