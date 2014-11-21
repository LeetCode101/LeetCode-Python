#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        lenA = len(A)
        lenB = len(B)
        total = lenA + lenB
        
        if total & 1:
            return self.getMedian(A, 0, lenA - 1, B, 0, lenB - 1, total / 2 + 1)
        else:
            return (self.getMedian(A, 0, lenA - 1, B, 0, lenB - 1, total / 2) + self.getMedian(A, 0, lenA - 1, B, 0, lenB - 1, total / 2 + 1)) / 2.0  
            
    def getMedian(self, A, startA, endA, B, startB, endB, k):
        m = endA - startA + 1
        n = endB - startB + 1
        
        if m > n:
            return self.getMedian(B, startB, endB, A, startA, endA, k)
        
        if m == 0:
            return B[k - 1]
        
        if k == 1:
            return min(A[startA], B[startB])
        
        pa = min(k / 2, m)
        pb = k - pa
        
        if A[startA + pa - 1] < B[startB + pb - 1]:
            return self.getMedian(A, startA + pa, endA, B, startB, endB, k - pa)
        elif A[startA + pa - 1] > B[startB + pb - 1]:
            return self.getMedian(A, startA, endA, B, startB + pb, endB, k - pb)
        else:
            return A[startA + pa - 1]