#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param {string} s
    # @return {boolean}
    def isNumber(self, s):
        s = s.strip()
        length = len(s)
        
        hasDot = False
        hasExponent = False
        hasNumber = False
        
        for i in range(length):
            c = s[i]
            
            if c <= '9' and c >= '0':
                hasNumber = True
            elif c == 'e':
                if hasExponent or not hasNumber:
                    return False
                
                hasNumber = False
                hasExponent = True
            elif c == '.':
                if hasDot or hasExponent:
                    return False
                
                hasDot = True
            elif c == '+' or c == '-':
                if i != 0 and s[i - 1] != 'e':
                    return False
            else:
                return False
        
        return hasNumber
