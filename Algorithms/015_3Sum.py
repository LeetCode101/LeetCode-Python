#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        results = []
        num.sort()
        length = len(num)
        m, n = 0, 0
        
        if length < 3:
            return results
        
        for i in range(length - 2):
            if i == 0 or num[i] > num[i - 1]:
                m, n = i + 1, length - 1
                
                while m < n:
                    if num[m] + num[n] == - num[i]:
                        results.append([num[i], num[m], num[n]])
                        
                        m += 1
                        n -= 1
                        
                        while m < n and num[m] == num[m - 1]:
                            m += 1
                        
                        while m < n and num[n] == num[n + 1]:
                            n -= 1
                    elif num[m] + num[n] > -num[i]:
                        n -= 1
                    else:
                        m += 1
        
        return results
