#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        length = len(A)
        low = 0
        high = length - 1
        mid = (low + high) >> 1
        
        while low <= high:
            current = A[mid]
            
            if current == target:
                start = mid
                end = mid
                
                while start - 1 >= low and A[start - 1] == current:
                    start -= 1
                
                while end + 1 <= high and A[end + 1] == current:
                    end += 1
                    
                return [start, end]
            elif current > target:
                high -= 1
            else:
                low += 1
            
            mid = (low + high) >> 1
        
        return [-1, -1]
