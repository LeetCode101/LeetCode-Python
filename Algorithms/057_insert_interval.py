#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @param {Interval} newInterval
    # @return {Interval[]}
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        
        result = []
        length = len(intervals)
        
        if length == 0:
            return result
        
        intervals.sort(self.compare)
        
        prev = intervals[0]
        
        for i in range(1, length):
            current = intervals[i]
            
            if prev.end < current.start:
                result.append(prev)
                prev = current
            else:
                prev = Interval(prev.start, max(prev.end, current.end))
        
        result.append(prev)
        
        return result
    
    def compare(self, a, b):
        return a.start - b.start
