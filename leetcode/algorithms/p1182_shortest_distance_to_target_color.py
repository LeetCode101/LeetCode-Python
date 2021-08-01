import bisect
import collections
from typing import List


class Solution:
    def shortestDistanceColor(self, colors: List[int],
                              queries: List[List[int]]) -> List[int]:
        positions = collections.defaultdict(list)
        result = []

        for i, color in enumerate(colors):
            positions[color].append(i)

        for i, color in queries:
            result.append(self._shortest(positions, i, color))

        return result

    def _shortest(self, positions, i, color):
        position = positions.get(color, [])

        if not position:
            return -1

        j = bisect.bisect_left(position, i)

        if j == 0:
            return abs(i - position[0])
        elif j == len(position):
            return abs(i - position[-1])
        else:
            return min(abs(i - position[j - 1]), abs(i - position[j]))
