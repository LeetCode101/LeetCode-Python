#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        integer = 0
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)
        
        while abs_dividend >= abs_divisor:
            shifts = 0
            
            while abs_dividend >= abs_divisor << shifts:
                shifts += 1
                
            integer += 1 << (shifts - 1)
            abs_dividend -= abs_divisor << (shifts - 1)
        
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            integer = -integer
        
        return 2147483647 if integer > 2147483647 else integer
