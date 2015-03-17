#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        length = len(A)
        index = 0
        
        if length == 0:
            return index
        
        for i in range(length):
            if A[index] == A[i]:
                continue
            
            index += 1
            A[index] = A[i]
        
        return index + 1