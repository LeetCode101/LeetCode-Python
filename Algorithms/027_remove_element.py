#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        length = len(A)
        index = 0
        
        if length == 0:
            return index
        
        for i in range(length):
            if A[i] == elem:
                continue
            
            A[index] = A[i]
            index += 1
        
        return index