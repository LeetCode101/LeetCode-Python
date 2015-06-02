#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        low = 0
        high = x
            
        while high >= low:
            mid = (low + high) / 2
            sqrt = mid * mid
            
            if sqrt < x:
                low = mid + 1
            elif sqrt > x:
                high = mid - 1
            else:
                return mid
        
        return high
