#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        length_a = len(A)
        length_b = len(B)
        total = length_a + length_b
        
        if total & 1:
            return self.getMedian(A, 0, length_a - 1, B, 0, length_b - 1, total / 2 + 1)
        else:
            return (self.getMedian(A, 0, length_a - 1, B, 0, length_b - 1, total / 2) + self.getMedian(A, 0, length_a - 1, B, 0, length_b - 1, total / 2 + 1)) / 2.0  
            
    def getMedian(self, A, start_a, end_a, B, start_b, end_b, k):
        length_a = end_a - start_a + 1
        length_b = end_b - start_b + 1
        
        if length_a > length_b:
            return self.getMedian(B, start_b, end_b, A, start_a, end_a, k)
        
        if length_a == 0:
            return B[k - 1]
        
        if k == 1:
            return min(A[start_a], B[start_b])
        
        pa = min(k / 2, length_a)
        pb = k - pa
        
        if A[start_a + pa - 1] < B[start_b + pb - 1]:
            return self.getMedian(A, start_a + pa, end_a, B, start_b, end_b, k - pa)
        elif A[start_a + pa - 1] > B[start_b + pb - 1]:
            return self.getMedian(A, start_a, end_a, B, start_b + pb, end_b, k - pb)
        else:
            return A[start_a + pa - 1]