#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        sum = ''
        carry = 0
        min_length = min(len(a), len(b))
        
        remained_binary = ''
        
        if len(a) > min_length:
            remained_binary = a[0:len(a) - min_length]
            a = a[len(a) - min_length:]
        elif len(b) > min_length:
            remained_binary = b[0:len(b) - min_length]
            b = b[len(b) - min_length:]

        for i in range(min_length - 1, -1, -1):
            if a[i] == '1' and b[i] == '1':
                sum = str(carry) + sum
                carry = 1
            elif a[i] != b[i]:
                if carry == 0:
                    sum = '1' + sum
                else:
                    sum = '0' + sum
                    carry = 1
            else:
                sum = str(carry) + sum
                carry = 0

        if carry == 0:
            return remained_binary + sum
        else:
            return self.plus_one(remained_binary) + sum
            
    def plus_one(self, s):
        sum = ''
        carry = 1
        length = len(s)

        if length == 0:
            return '1'
        
        for i in range(length - 1, -1, -1):
            if carry == 1:
                if s[i] == '0':
                    sum = '1' + sum
                    carry = 0
                else:
                    sum = '0' + sum
            else:
                sum = s[i] + sum

        return sum if sum[0] != '0' else '1' + sum
