from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        sorted_intervals = [(interval, i) for i, interval
                            in enumerate(intervals)]
        sorted_intervals = sorted(sorted_intervals, key=lambda x: x[0][0])
        result = [-1] * n

        for i, interval in enumerate(sorted_intervals):
            end = interval[0][1]
            j = self._binary_search(sorted_intervals, i, n - 1, end)

            if j < n:
                result[interval[1]] = sorted_intervals[j][1]

        return result

    def _binary_search(self, intervals, low, high, target):
        while low <= high:
            middle = low + (high - low) // 2
            start, end = intervals[middle][0]

            if start == target:
                return middle
            elif start > target:
                high = middle - 1
            else:
                low = middle + 1

        return low
