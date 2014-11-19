#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        mapping = {}
        
        for index, value in enumerate(num):
            if value in mapping:
                return (mapping[value] + 1, index + 1)
            else:
                mapping[target - value] = index