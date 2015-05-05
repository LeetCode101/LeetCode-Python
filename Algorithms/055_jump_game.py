#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        max_reachable_index_ending_here = 0
        
        for i in range(len(nums)):
            if max_reachable_index_ending_here >= i:
                max_reachable_index_ending_here = max(max_reachable_index_ending_here, i + nums[i])
        
        if max_reachable_index_ending_here >= len(nums) - 1:
            return True
        else:
            return False
