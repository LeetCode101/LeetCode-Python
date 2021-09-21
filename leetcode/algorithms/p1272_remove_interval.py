from typing import List


class Solution:
    def removeInterval(self, intervals: List[List[int]],
                       toBeRemoved: List[int]) -> List[List[int]]:
        result = []
        i, n = 0, len(intervals)

        while i < n and intervals[i][1] <= toBeRemoved[0]:
            result.append(intervals[i])
            i += 1

        if i < n and intervals[i][0] <= toBeRemoved[0] \
                and toBeRemoved[1] <= intervals[i][1]:
            if intervals[i][0] != toBeRemoved[0]:
                result.append([intervals[i][0], toBeRemoved[0]])

            if intervals[i][1] != toBeRemoved[1]:
                result.append([toBeRemoved[1], intervals[i][1]])

            i += 1
        elif i < n and intervals[i][0] <= toBeRemoved[0] <= intervals[i][1]:
            result.append([intervals[i][0], toBeRemoved[0]])

            i += 1

        while i < n and toBeRemoved[0] <= intervals[i][0] \
                and intervals[i][1] <= toBeRemoved[1]:
            i += 1

        if i < n and intervals[i][0] <= toBeRemoved[1] <= intervals[i][1]:
            result.append([toBeRemoved[1], intervals[i][1]])
            i += 1

        result.extend(intervals[i:])

        return result
