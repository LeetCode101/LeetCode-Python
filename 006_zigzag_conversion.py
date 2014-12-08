#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return a string
    def convert(self, s, nRows):
        result = ''
        length = len(s)
        
        if nRows == 1:
            return s
            
        for row in range(0, nRows):
            i = 0
            index = 0
            
            while True:
                if row == 0 or row == nRows - 1:
                    index = row + 2 * (nRows - 1) * i
                else:
                    if i & 1:
                        index = row + (nRows - 1 - row) * 2 + 2 * (nRows - 1) * (i - 1) / 2
                    else:
                        index = row + 2 * (nRows - 1) * i / 2 
            
                if index > length - 1:
                    break
                
                result += s[index]
                
                i += 1
                
        return result