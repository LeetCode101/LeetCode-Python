#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        length = len(nums)
        
        if length <= 2:
            return length
        
        end = 1
        
        for i in range(2, length):
            if nums[i] != nums[end - 1]:
                end += 1
                
                nums[end] = nums[i]
        
        return end + 1
