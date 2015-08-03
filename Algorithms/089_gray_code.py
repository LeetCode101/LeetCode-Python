#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param {integer} n
    # @return {integer[]}
    def grayCode(self, n):
        count = 2 ** n
        
        return [(i >> 1) ^ i for i in range(count)]
