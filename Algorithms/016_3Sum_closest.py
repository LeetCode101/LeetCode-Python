#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        results = []
        num.sort()
        length = len(num)
        m, n = 0, 0
        diff_abs_so_far, diff_abs_current, diff_current = 2147483647, 0, 0
        
        for i in range(length - 2):
            if i == 0 or num[i] > num[i - 1]:
                m, n = i + 1, length - 1
                
                while m < n:
                    diff_current = num[m] + num[n] + num[i] - target
                    diff_abs_current = abs(diff_current)
                    
                    if diff_abs_so_far > diff_abs_current:
                        diff_abs_so_far = diff_abs_current
                        results = [num[i], num[m], num[n]]
                        
                    if diff_current == 0:
                        return sum(results)
                    if diff_current > 0:
                        n -= 1
                    else:
                        m += 1
                
        return sum(results)
