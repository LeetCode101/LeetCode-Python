#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        i = 0
        length = len(A)
        
        while i < length:
            current = A[i]
            
            if current != i + 1 and current > 0 and current <= length and current != A[current - 1]:
                A[i], A[current - 1] = A[current - 1], A[i]
            else:
                i += 1
        
        for i in range(length):
            if A[i] != i + 1:
                return i + 1
            
        return length + 1
