from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        sorted_points = sorted(points, key=lambda x: x[0])
        count = 0
        i = 0

        while i < len(sorted_points):
            start, end = sorted_points[i]
            j = i + 1

            while j < len(sorted_points) \
                    and start <= sorted_points[j][0] <= end:
                j += 1

            count += 1
            i = j

        return count
