#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        combination = []
        combination_candidates = []
        
        candidates.sort()
        
        self.find_combinations(candidates, target, 0, combination_candidates, combination)
        
        return combination
        
    def find_combinations(self, candidates, target, start, combination_candidates, combination):
        if target < 0:
            return
        
        if target == 0:
            combination.append(combination_candidates[:])
            
            return
        
        for i in range(start, len(candidates)):
            current = candidates[i]
            
            if i > 0 and current == candidates[i - 1]:
                continue
            
            combination_candidates.append(current)
            
            self.find_combinations(candidates, target - current, i, combination_candidates, combination)
            
            combination_candidates.pop()
