#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        string_length = len(s)
        pattern_length = len(p)
        
        table = [[False] * (pattern_length + 1) for i in range(string_length + 1)]
        table[0][0] = True
        
        for i in range(1, pattern_length + 1):
            if p[i - 1] == '*' and table[0][i - 2]:
                table[0][i] = True

        for i in range(1, string_length + 1):
            for j in range(1, pattern_length + 1):
                char = s[i - 1]
                pattern = p[j - 1]
                
                if pattern == '*':
                    if table[i][j - 2]:
                        table[i][j] = True
                    elif self.match(char, p[j - 2]) and table[i - 1][j]:
                        table[i][j] = True
                else:
                    if self.match(char, pattern) and table[i - 1][j - 1]:
                        table[i][j] = True
        
        return table[string_length][pattern_length]
        
    def match(self, char, pattern):
        return char == pattern or pattern == '.'
