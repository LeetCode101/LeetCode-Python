#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param {string} s1
    # @param {string} s2
    # @return {boolean}
    def isScramble(self, s1, s2):
        if s1 == s2:
            return True
        
        length = len(s1)
        char_count = {}
        
        for i in range(length):
            char1 = s1[i]
            char2 = s2[i]
            
            if not char1 in char_count:
                char_count[char1] = 1
            else:
                char_count[char1] += 1
            
            if not char2 in char_count:
                char_count[char2] = -1
            else:
                char_count[char2] -= 1
        
        for key in char_count:
            if char_count[key] != 0:
                return False
        
        for i in range(1, length):
            if self.isScramble(s1[0:i], s2[0:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            
            if self.isScramble(s1[0:i], s2[length - i:]) and self.isScramble(s1[i:], s2[0:length - i]):
                return True
        
        return False    
