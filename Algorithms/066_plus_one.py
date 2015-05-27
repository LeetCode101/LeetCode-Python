#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        carry = 1
        length = len(digits)
            
        for i in range(length - 1, -1, -1):
            if digits[i] + carry == 10:
                carry = 1
                digits[i] = 0
            else:
                digits[i] += carry
                
                break
        
        return digits if digits[0] != 0 else [1] + digits
