import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            first, second = heapq.heappop(heap), heapq.heappop(heap)

            if first != second:
                heapq.heappush(heap, first - second)

        return 0 if not heap else -heap[0]
