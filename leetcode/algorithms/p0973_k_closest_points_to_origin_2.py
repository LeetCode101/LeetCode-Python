from heapq import heapify, heappush, heappop
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if not points:
            return []

        heap = [(-(pow(points[0][0], 2) + pow(points[0][1], 2)), 0)]
        heapify(heap)

        for i in range(1, len(points)):
            heappush(heap, (-(pow(points[i][0], 2) + pow(points[i][1], 2)), i))

            if len(heap) > K:
                heappop(heap)

        return [points[x[1]] for x in heap]
