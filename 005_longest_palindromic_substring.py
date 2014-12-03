#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return a string
    def longestPalindrome(self, s):
        length = len(s)
        
        if length == 1:
            return s
            
        max_length = 1
        max_length_start = 0
        max_length_end = 0
        
        low = 0
        high = 0
        
        for i in range(1, length):
            low = i - 1
            high = i
            
            while low >= 0 and high < length and s[low] == s[high]:
                current_length = high - low + 1
                
                if current_length > max_length:
                    max_length = current_length
                    max_length_start = low
                    max_length_end = high
                
                low -= 1
                high += 1
                
            low = i - 1
            high = i + 1
            
            while low >= 0 and high < length and s[low] == s[high]:
                current_length = high - low + 1
                
                if current_length > max_length:
                    max_length = current_length
                    max_length_start = low
                    max_length_end = high
                    
                low -= 1
                high += 1
                
        return s[max_length_start:max_length_end + 1]