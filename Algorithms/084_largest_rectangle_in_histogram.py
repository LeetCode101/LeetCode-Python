#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height):
        height = height + [0]
        max_area = 0
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
