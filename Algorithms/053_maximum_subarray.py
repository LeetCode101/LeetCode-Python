#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        max_so_far, max_ending_here = nums[0], nums[0]
        
        for n in nums[1:]:
            max_ending_here = max(max_ending_here + n, n)
            max_so_far = max(max_so_far, max_ending_here)
        
        return max_so_far
