#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        if n < 3:
            return n
            
        steps = [0] * n
        steps[0] = 1
        steps[1] = 2
        
        for i in range(2, n):
            steps[i] = steps[i - 1] + steps[i - 2]
        
        return steps[n - 1]
