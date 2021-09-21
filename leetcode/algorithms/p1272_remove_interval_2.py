from typing import List


class Solution:
    def removeInterval(self, intervals: List[List[int]],
                       toBeRemoved: List[int]) -> List[List[int]]:
        result = []

        for start, end in intervals:
            if end <= toBeRemoved[0] or start >= toBeRemoved[1]:
                result.append([start, end])
            elif start >= toBeRemoved[0] and end <= toBeRemoved[1]:
                continue
            else:
                if start < toBeRemoved[0] < end:
                    result.append([start, toBeRemoved[0]])

                if start < toBeRemoved[1] < end:
                    result.append([toBeRemoved[1], end])

        return result
