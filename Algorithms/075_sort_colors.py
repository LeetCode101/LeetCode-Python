#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        index_after_red = 0
        index_after_white = 0
        index_before_blue = len(nums) - 1
        
        while index_after_white <= index_before_blue:
            color = nums[index_after_white]
            
            if color == 0:
                self.swap(nums, index_after_red, index_after_white)
                
                index_after_red += 1
                index_after_white += 1
            elif color == 1:
                index_after_white += 1
            elif color == 2:
                self.swap(nums, index_after_white, index_before_blue)
                
                index_before_blue -= 1
            
    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]
