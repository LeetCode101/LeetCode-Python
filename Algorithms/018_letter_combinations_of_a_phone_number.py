#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        mapping = {
            '0': '',
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        letters = [mapping[digit] for digit in digits]
        
        return self.letterCombinationsInternal(letters)
            
    def letterCombinationsInternal(self, letters):
        length = len(letters)
            
        if length == 0:
            return ['']
            
        if length == 1:
            return self.string_to_list(letters[0])
        
        results = []
        mid = (length - 1) >> 1
        
        left = self.letterCombinationsInternal(letters[0:mid + 1])
        right = self.letterCombinationsInternal(letters[mid + 1:])
        
        left_length = len(left)
        right_length = len(right)
        
        for i in range(0, left_length):
            for j in range(0, right_length):
                results.append(left[i] + right[j])
        
        return results
    
    def string_to_list(self, string):
        return list(string) if string != '' else ['']
