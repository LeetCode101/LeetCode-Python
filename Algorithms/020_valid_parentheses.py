#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        
        for c in s:
            if self.is_left_parenthesis(c):
                stack.append(c)
            elif len(stack) == 0:
                return False
            elif not self.is_match(stack.pop(), c):
                return False
                        
        return True if len(stack) == 0 else False
        
    def is_left_parenthesis(self, s):
        return s == '(' or s == '{' or s == '['
        
    def is_match(self, left, right):
        if left == '(':
            return right == ')'
        elif left == '{':
            return right == '}'
        elif left == '[':
            return right == ']'
