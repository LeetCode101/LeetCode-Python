#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        m, n = 0, 0
        min_diff_sum, length = 0, len(num)
        diff_abs_so_far, diff_abs_current, diff_current = 2147483647, 0, 0
        
        for i in range(length - 2):
            if i == 0 or num[i] > num[i - 1]:
                m, n = i + 1, length - 1
                
                while m < n:
                    diff_current = num[m] + num[n] + num[i] - target
                    diff_abs_current = abs(diff_current)
                    
                    if diff_abs_so_far > diff_abs_current:
                        diff_abs_so_far = diff_abs_current
                        min_diff_sum = sum([num[i], num[m], num[n]])
                        
                    if diff_current == 0:
                        return min_diff_sum
                    elif diff_current > 0:
                        n -= 1
                    else:
                        m += 1
                
        return min_diff_sum
