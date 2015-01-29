#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        length = len(A)
        
        if length < 2:
            return length
            
        current, max_so_far = 0, A[0]
        new_length, available_index = 1, []
        
        for i in range(1, length):
            current = A[i]
            
            if current > max_so_far:
                max_so_far = current
                new_length += 1
                
                if len(available_index) > 0:
                    A[available_index.pop(0)] = current
                    available_index.append(i)
            else:
                available_index.append(i)
        
        return new_length