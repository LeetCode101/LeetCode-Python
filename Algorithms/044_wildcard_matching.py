#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param s, an input string
    # @param p, a pattern string
    # @return a boolean
    def isMatch(self, s, p):
        char_index = 0
        pattern_index = 0
        prev_char_matches_star_index = 0
        prev_star_index = -1
        
        string_length = len(s)
        pattern_length = len(p)
        
        while char_index < string_length:
            if pattern_index < pattern_length and (s[char_index] == p[pattern_index] or p[pattern_index] == '?'):
                char_index += 1
                pattern_index += 1
            elif pattern_index < pattern_length and p[pattern_index] == '*':
                prev_char_matches_star_index = char_index
                prev_star_index = pattern_index
                pattern_index += 1
            elif prev_star_index != -1:
                pattern_index = prev_star_index + 1
                prev_char_matches_star_index += 1
                char_index = prev_char_matches_star_index
            else:
                return False
        
        while pattern_index < pattern_length and p[pattern_index] == '*':
            pattern_index += 1
        
        if pattern_index == pattern_length:
            return True
        else:
            return False
