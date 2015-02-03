#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        length_string, length_list = len(S), len(L)
        
        if length_string == 0 or length_list == 0:
            return []
        
        length_word = len(L[0])
        length_words = length_word * length_list
        
        results = []
        words = {}
        
        for word in L:
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
            
        for i in range(0, length_string - length_words + 1):
            sub_string = S[i:i + length_words]
            
            if self.is_valid_sub_string(sub_string, words.copy(), length_word):
                results.append(i)
        
        return results
            
    def is_valid_sub_string(self, s, words, length_word):
        for i in range(0, len(s), length_word):
            word = s[i:i + length_word]
            
            if word in words:
                value = words[word]
            else:
                return False
            
            if value == 0:
                return False
            else:
                words[word] -= 1
        
        return True
