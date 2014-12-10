#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
            
        length = 1 if x == 0 else int(math.floor(math.log(x, 10))) + 1
        
        while length > 1:
            first_digit_pow = pow(10, length - 1)
            first_digit = x / first_digit_pow
            last_digit = x % 10
            
            if first_digit == last_digit:
                x -= first_digit * first_digit_pow
                x /= 10
                length -= 2
            else:
                return False
        
        return True
