#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return an integer
    def atoi(self, str):
        str = str.strip()
        
        if len(str) == 0:
            return 0
        
        sign = ''
        integer = 0
        digits = []
        
        if str[0] == '+' or str[0] == '-':
            sign = str[0]
            str = str[1:]
        
        for c in str:
            if c >= '0' and c <= '9':
                digits.append(int(c))
            else:
                break
        
        length = len(digits)
        
        for i in range(length):
            integer += digits[i] * pow(10, length - 1 - i)
        
        if sign == '-':
            integer *= -1
        
        INT_MAX = 2147483647
        INT_MIN = - 2147483648
        
        if integer > INT_MAX:
            return INT_MAX
        elif integer < INT_MIN:
            return INT_MIN
        else:
            return integer
