from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        sorted_intervals = [(interval, i) for i, interval in enumerate(intervals)]
        sorted_intervals = sorted(sorted_intervals, key=lambda x: x[0][0])
        result = [-1] * n

        for i, interval in enumerate(sorted_intervals):
            j = i + 1

            while j < n and interval[0][1] > sorted_intervals[j][0][0]:
                j += 1

            if j < n:
                result[interval[1]] = sorted_intervals[j][1]

        return result
