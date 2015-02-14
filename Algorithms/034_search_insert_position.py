#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        length = len(A)
        low = 0
        high = length - 1
        mid = (low + high) >> 1
        
        while low <= high:
            current = A[mid]
            
            if current == target:
                return mid
            
            if current > target:
                high = mid - 1
            else:
                low = mid + 1
        
            mid = (low + high) >> 1
        
        return low
