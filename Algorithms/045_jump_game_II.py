#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        steps = 0
        max_reachable_index_so_far = 0
        max_reachable_index_ending_here = 0
        
        for i in range(len(A)):
            if i > max_reachable_index_so_far:
                steps += 1
                max_reachable_index_so_far = max_reachable_index_ending_here
            
            max_reachable_index_ending_here = max(max_reachable_index_ending_here, i + A[i])
        
        return steps
