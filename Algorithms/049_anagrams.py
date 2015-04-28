#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        dict = {}
        result = []
        
        for index, string in enumerate(strs):
            sorted_string = ''.join(sorted(string))
            
            if sorted_string in dict:
                if dict[sorted_string] != -1:
                    result.append(strs[dict[sorted_string]])
                    
                    dict[sorted_string] = -1
                    
                result.append(string)
            else:
                dict[sorted_string] = index
        
        return result
