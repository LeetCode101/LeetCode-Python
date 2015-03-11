#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        length = len(A)
        max_area = 0
        max_hight_index = 0
        max_height_so_far = 0
        
        for i in range(length):
            if A[i] > A[max_hight_index]:
                max_hight_index = i
        
        for i in range(max_hight_index):
            current = A[i]
            
            if current < max_height_so_far:
                max_area += max_height_so_far - current
            else:
                max_height_so_far = current
        
        max_height_so_far = 0
        
        for i in range(length - 1, max_hight_index, -1):
            current = A[i]
            
            if current < max_height_so_far:
                max_area += max_height_so_far - current
            else:
                max_height_so_far = current
        
        return max_area
