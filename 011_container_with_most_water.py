#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return an integer
    def maxArea(self, height):
        max_area = 0
        max_area_so_far = 0
        left, right = 0, len(height) - 1
        
        while left < right:
            left_height, right_height = height[left], height[right]
            max_area_so_far = min(left_height, right_height) * (right - left)
            max_area = max(max_area, max_area_so_far)
            
            if left_height < right_height:
                left += 1
            else:
                right -= 1
        
        return max_area
