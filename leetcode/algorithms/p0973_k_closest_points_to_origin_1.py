from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distance = sorted(points, key=lambda x: pow(x[0], 2) + pow(x[1], 2))

        return distance[:K]
