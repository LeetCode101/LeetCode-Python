#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        length = len(A)
        low = 0
        high = length - 1
        mid = (low + high) >> 1
        
        while low <= high:
            current = A[mid]
            
            if current == target:
                return mid
            
            if current >= A[high]:
                if A[low] <= target and target < current:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if target > current and target <= A[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            
            mid = (low + high) >> 1
        
        return -1
