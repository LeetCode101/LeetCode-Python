#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {boolean}
    def search(self, nums, target):
        length = len(nums)
        low = 0
        high = length - 1
        mid = (low + high) >> 1
        
        while low <= high:
            current = nums[mid]
            
            if current == target:
                return True
            
            if current > nums[high]:
                if nums[low] <= target and target < current:
                    high = mid - 1
                else:
                    low = mid + 1
            elif current < nums[high]:
                if target > current and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                high -= 1
            
            mid = (low + high) >> 1
        
        return False
