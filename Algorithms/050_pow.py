#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        return self.pow(x, n) if n >= 0 else 1.0 / self.pow(x, -n)
            
    def pow(self, x, n):
        if n == 0:
            return 1.0
        
        half = self.pow(x, n / 2)
        
        return half * half if n & 1 == 0 else half * half * x
