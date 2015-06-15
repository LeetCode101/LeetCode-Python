#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        permutation = ''
        available_numbers = [i for i in range(1, n + 1)]
        
        for i in range(n):
            group_count = self.factorial(n - 1 - i)
            group_number = int(math.ceil(k * 1.0 / group_count))
            permutation += str(available_numbers[group_number - 1])
            
            del available_numbers[group_number - 1]
            
            k -= group_count * (group_number - 1)
        
        return permutation
    
    def factorial(self, n):
        result = 1
        
        for i in range(2, n + 1):
            result *= i
        
        return result
