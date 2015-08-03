#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):
        nums.sort()
        
        combinations = []
        length = len(nums)
        
        for i in range(length + 1):
            combination = []
            
            self.combine(length, 0, i, combination, combinations, nums)
        
        return combinations
    
    def combine(self, n, start, k, combination, combinations, nums):
        if k == 0:
            combinations.append(combination)
            
            return
        
        for i in range(start, n):
            if i != start and nums[i] == nums[i - 1]:
                continue
            
            combination.append(nums[i])
            
            self.combine(n, i + 1, k - 1, combination[:], combinations, nums)
            
            combination.pop()
