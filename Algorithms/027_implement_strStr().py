#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        length_haystack, length_needle = len(haystack), len(needle)
        
        if length_haystack == 0 and length_needle == 0:
            return 0
        
        for i in range(length_haystack):
            if length_haystack - i < length_needle:
                break
            
            temp = i
            
            for j in range(length_needle):
                if haystack[temp] == needle[j]:
                    temp += 1
                else:
                    break
            
            if temp - i == length_needle:
                return i
        
        return -1
