from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) \
            -> List[List[int]]:
        sorted_intervals = sorted(intervals + [newInterval],
                                  key=lambda x: x[0])
        merged = [sorted_intervals[0]]

        for i in range(1, len(sorted_intervals)):
            top = merged[-1]
            current = sorted_intervals[i]

            if top[0] <= current[0] <= top[1]:
                merged[-1][1] = max(merged[-1][1], current[1])
            else:
                merged.append(current)

        return merged
