#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def minDistance(self, word1, word2):
        word1_length = len(word1)
        word2_length = len(word2)
        table = [[0] * (word2_length + 1) for i in range(word1_length + 1)]
        
        for i in range(1, word2_length + 1):
            table[0][i] = i
        
        for i in range(1, word1_length + 1):
            table[i][0] = i
        
        for i in range(1, word1_length + 1):
            for j in range(1, word2_length + 1):
                # Example: 'ab' - > 'abc'
                # 'a' -> 'abc' + 'b' -> ''
                possibility1 = table[i - 1][j] + 1
                
                # 'ab' -> 'ab' + '' -> ''
                possibility2 = table[i][ j - 1] + 1
                
                # 'a' -> 'ab' + 'b' -> 'c'
                possibility3 = table[i - 1][j - 1] + (0 if word1[i - 1] == word2[j - 1] else 1)
                
                table[i][j] = min(possibility1, possibility2, possibility3)
        
        return table[word1_length][word2_length]
