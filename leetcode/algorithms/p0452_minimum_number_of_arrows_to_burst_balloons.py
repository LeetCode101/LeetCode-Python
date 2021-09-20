import sys
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        sorted_points = sorted(points, key=lambda x: x[1])
        count = 0
        end = -sys.maxsize

        for point in sorted_points:
            if point[0] > end:
                count += 1
                end = point[1]

        return count
