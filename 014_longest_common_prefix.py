#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        strs.sort()
        length = len(strs)
        
        if length == 0:
            return ''
        
        common, first_str, last_str = '', strs[0], strs[length - 1]
        
        for i in range(len(first_str)):
            if first_str[i] == last_str[i]:
                common += first_str[i]
            else:
                break
        
        return common
