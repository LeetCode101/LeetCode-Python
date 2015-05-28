#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        sum = ''
        carry = 0
        index_a = len(a) - 1
        index_b = len(b) - 1

        while index_a >= 0 or index_b >= 0:
            char_a = a[index_a] if index_a >= 0 else '0'
            char_b = b[index_b] if index_b >= 0 else '0'
            
            if char_a == '1' and char_b == '1':
                sum = str(carry) + sum
                carry = 1
            elif char_a != char_b:
                if carry == 0:
                    sum = '1' + sum
                else:
                    sum = '0' + sum
                    carry = 1
            else:
                sum = str(carry) + sum
                carry = 0
            
            index_a -= 1
            index_b -= 1

        return sum if carry == 0 else '1' + sum
