#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        results = []
        
        self.generate_parenthesis_internal(n, 0, 0, '', results)
        
        return results
    
    def generate_parenthesis_internal(self, n, left, right, s, results):
        if left == n:
            results.append(s + ')' * (n - right))
        elif left > right:
            self.generate_parenthesis_internal(n, left + 1, right, s + '(', results)
            self.generate_parenthesis_internal(n, left, right + 1, s + ')', results)
        elif left == right:
            self.generate_parenthesis_internal(n, left + 1, right, s + '(', results)
