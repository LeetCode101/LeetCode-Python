#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {string}
    def minWindow(self, s, t):
        letters_in_t = {}
        
        for char in t:
            if char not in letters_in_t:
                letters_in_t[char] = 1
            else:
                letters_in_t[char] += 1
        
        start = 0
        end = 0
        length_s = len(s)
        length_t = len(t)
        matched_letters_count = 0
        min_window = ''
        min_window_length = length_s + 1
        matched_letters_in_s = {}
        
        while end < length_s:
            char = s[end]
            
            if char in letters_in_t:
                if char in matched_letters_in_s:
                    matched_letters_in_s[char] += 1
                else:
                    matched_letters_in_s[char] = 1
                
                if matched_letters_in_s[char] <= letters_in_t[char]:
                    matched_letters_count += 1
            
            if matched_letters_count == length_t:
                char = s[start]
                
                while start <= end:
                    if char not in matched_letters_in_s:
                        pass
                    elif matched_letters_in_s[char] > letters_in_t[char]:
                        matched_letters_in_s[char] -= 1
                    else:
                        break
                    
                    start += 1
                    char = s[start]
                
                if end - start + 1 < min_window_length:
                    min_window = s[start: end + 1]
                    min_window_length = end - start + 1
            
            end += 1
        
        return min_window
