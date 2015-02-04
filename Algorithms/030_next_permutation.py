#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param num, a list of integer
    # @return a list of integer
    def nextPermutation(self, num):
        length = len(num)
        
        if length == 0:
            return num
            
        i = -1
        max_so_far = num[length - 1]
        
        for i in range(length - 1, -1, -1):
            current = num[i]
            
            if current >= max_so_far:
                max_so_far = num[i]
            else:
                for j in range(length - 1, i, -1):
                    if current < num[j]:
                        num[i], num[j] = num[j], num[i]
                        break
                
                return self.reverse(num, i + 1, length - 1)
        
        if i == 0:
            num.reverse()
        
        return num
    
    def reverse(self, num, start, end):
        while start < end:
            num[start], num[end] = num[end], num[start]
            
            start += 1
            end -= 1
        
        return num
