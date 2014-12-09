#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return an integer
    def reverse(self, x):
        digit = 0
        reversed_x = 0
        abs_x = abs(x)
        isNegative = x < 0
        max_abs_x = 2147483648 if x < 0 else 2147483647
        
        while abs_x:
            digit = abs_x % 10
            reversed_x = reversed_x * 10 + digit
            abs_x /= 10
        
        if reversed_x > max_abs_x:
            return 0
        else:
            return reversed_x * -1 if isNegative else reversed_x
