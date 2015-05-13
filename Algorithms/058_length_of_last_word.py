#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        start = len(s) - 1
        last_word_length = 0
        
        while start >= 0 and s[start] == ' ':
            start -= 1
        
        while start >= 0:
            if s[start] == ' ':
                break
            else:
                last_word_length += 1
            
            start -= 1
        
        return last_word_length
