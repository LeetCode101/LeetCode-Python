#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return a string
    def intToRoman(self, num):
        result = ''
        symbol = {}
        digit, p, length = 0, 0, 0
        symbols = [
            {
                'symbol': 'I',
                'symbol_for_five': 'V',
                'symbol_for_ten': 'X'
            },
            {
                'symbol': 'X',
                'symbol_for_five': 'L',
                'symbol_for_ten': 'C'
            },
            {
                'symbol': 'C',
                'symbol_for_five': 'D',
                'symbol_for_ten': 'M'
            },
            {
                'symbol': 'M',
                'symbol_for_five': '',
                'symbol_for_ten': ''
            }
        ]
        
        while num > 0:
            length = len(str(num))
            p = pow(10, length - 1)
            digit = num / p
            num -= digit * p
            symbol = symbols[length - 1]
               
            if digit < 4:
                result += symbol['symbol'] * digit
            elif digit == 4:
                result += symbol['symbol'] + symbol['symbol_for_five']
            elif digit == 5:
                result += symbol['symbol_for_five']
            elif digit < 9:
                result += symbol['symbol_for_five'] + symbol['symbol'] * (digit - 5)
            else:
                result += symbol['symbol'] + symbol['symbol_for_ten']
        
        return result