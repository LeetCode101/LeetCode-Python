#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
        combination = []
        combinations = []
        
        self.combine_internal(n, 1, k, combination, combinations)
        
        return combinations
    
    def combine_internal(self, n, start, k, combination, combinations):
        if k == 0:
            combinations.append(combination)
            
            return
        
        for i in range(start, n - k + 2):
            combination.append(i)
            self.combine_internal(n, i + 1, k - 1, combination[:], combinations)
            combination.pop()
