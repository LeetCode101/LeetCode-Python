#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        mapping = {}
        
        # If num1 is in the array, then (target - num1) must be also in the array
        for index, value in enumerate(num):
            if target - value in mapping:
                return (mapping[target - value] + 1, index + 1)
            else:
                mapping[value] = index