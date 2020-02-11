from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        stack = [intervals[0]]

        for i in range(1, len(intervals)):
            top = stack[-1]
            current = intervals[i]

            if top[0] <= current[0] <= top[1]:
                stack[-1][1] = max(stack[-1][1], current[1])
            else:
                stack.append(current)

        return stack
