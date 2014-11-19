#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        index1 = 0
        index2 = 0
        mapping = {}
        
        for index, value in enumerate(num):
            if value in mapping:
                index1 = mapping[value] + 1
                index2 = index + 1
                return (index1, index2)
            else:
                mapping[target - value] = index