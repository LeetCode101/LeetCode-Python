#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = 0
        max_length = 0
        last_index_of_letter = {}
        
        for index, value in enumerate(s):
            if value in last_index_of_letter:
                max_length = max(index - start, max_length)
                
                # Remove the last index of letters from s[start] to s[last_index_of_letter[value] - 1]
                for i in range(start, last_index_of_letter[value]):
                    del last_index_of_letter[s[i]]
                    
                start = last_index_of_letter[value] + 1
                
                # Reset last index of current duplicate letter
                last_index_of_letter[value] = index
            else:
                last_index_of_letter[value] = index
                max_length = max(index - start + 1, max_length)
        
        return max_length
