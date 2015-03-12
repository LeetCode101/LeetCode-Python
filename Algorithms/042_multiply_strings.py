#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        length_num1 = len(num1)
        length_num2 = len(num2)
        digits = [0] * (length_num1 + length_num2)
        
        for i in range(length_num1):
            m = int(num1[i])
            
            for j in range(length_num2):
                n = int(num2[j])
                digits[i + j] += m * n
        
        result = ''
        
        for i in range(length_num1 + length_num2):
            current = digits[i]
            result = str(current % 10) + result
            
            if current > 9:
                digits[i + 1] += current / 10
        
        index = -1
        
        for i in range(length_num1 + length_num2):
            if result[i] == '0':
                index += 1
            else:
                break
        
        if index == len(result) - 1:
            result = '0'
        elif index > -1:
            result = result[index + 1:]
            
        return result
