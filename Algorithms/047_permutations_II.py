#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        permutations = []

        self.permuteInternal(num, 0, len(num) - 1, permutations)
        
        return permutations
    
    def permuteInternal(self, num, i, max_index, permutations):
        if i == max_index:
            permutations.append(num)
        else:
            for j in range(i, max_index + 1):
                duplicate = False
                
                for m in range(i, j):
                    if num[m] == num[j]:
                        duplicate = True
                        break
                
                if duplicate:
                    continue
                
                num[j], num[i] = num[i], num[j]
                
                self.permuteInternal(num[:], i + 1, max_index, permutations)
                
                num[j], num[i] = num[i], num[j]
