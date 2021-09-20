from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        sorted_intervals = sorted(intervals, key=lambda x: x[1])
        end = sorted_intervals[0][1]
        count = 0

        for i in range(1, len(sorted_intervals)):
            if end > sorted_intervals[i][0]:
                count += 1
            else:
                end = sorted_intervals[i][1]

        return count
