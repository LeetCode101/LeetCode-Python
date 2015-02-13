#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        length = len(s)
        max_length = 0
        stack = []
        start = 0
        
        for i in range(length):
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) == 0:
                    start = i + 1
                else:
                    stack.pop()
                    
                    if len(stack) == 0:
                        max_length = max(max_length, i - start + 1)
                    else:
                        max_length = max(max_length, i - stack[-1])
        
        return max_length
