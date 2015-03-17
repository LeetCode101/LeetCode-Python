#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return a string
    def countAndSay(self, n):
        if n == 1:
            return '1'
        
        sequence = ''
        prev_sequence = '1'
        
        while n > 1:
            count = 1
            sequence = ''
            
            for i in range(1, len(prev_sequence)):
                if prev_sequence[i] == prev_sequence[i - 1]:
                    count += 1
                else:
                    sequence += str(count)
                    sequence += prev_sequence[i - 1]
                    count = 1
                    
            sequence += str(count)
            sequence += prev_sequence[-1]
            
            n -= 1
            prev_sequence = sequence
        
        return sequence
