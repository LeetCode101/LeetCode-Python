#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    def __init__(self):
        self.max_length_start = 0
        self.max_length_end = 0
        
    # @return a string
    def longestPalindrome(self, s):
        low = 0
        high = 0
        length = len(s)
        
        for i in range(1, length):
            low = i - 1
            high = i
            
            # Find the longest even length palindrome string
            self.find_the_longest_palindrome(low, high, s, length)
                
            low = i - 1
            high = i + 1
            
            # Find the longest odd length palindrome string
            self.find_the_longest_palindrome(low, high, s, length)
                
        return s[self.max_length_start:self.max_length_end + 1]
        
    def find_the_longest_palindrome(self, low, high, s, length):
        while low >= 0 and high < length and s[low] == s[high]:
            current_length = high - low + 1
            current_max_length = self.max_length_end - self.max_length_start + 1
            
            if current_length > current_max_length:
                self.max_length_start = low
                self.max_length_end = high
            
            low -= 1
            high += 1