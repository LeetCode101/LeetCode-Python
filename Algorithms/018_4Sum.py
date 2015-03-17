#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        results = []
        num.sort()
        length = len(num)
        m, n = 0, 0
        
        if length < 4:
            return results
        
        for i in range(length - 3):
            if i != 0 and num[i] <= num[i - 1]:
                continue
            
            for j in range(i + 1, length - 2):
                if j != i + 1 and num[j] <= num[j - 1]:
                    continue
                
                m, n = j + 1, length - 1
                
                while m < n:
                    if num[i] + num[j] + num[m] + num[n] == target:
                        results.append([num[i], num[j], num[m], num[n]])
                        
                        m += 1
                        n -= 1
                        
                        while m < n and num[m] == num[m - 1]:
                            m += 1
                        
                        while m < n and num[n] == num[n + 1]:
                            n -= 1
                    elif num[i] + num[j] + num[m] + num[n] > target:
                        n -= 1
                    else:
                        m += 1
        
        return results
