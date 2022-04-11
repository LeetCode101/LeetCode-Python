import heapq
import sys
from typing import List


class Solution:
    def mincostToHireWorkers(self, quality: List[int],
                             wage: List[int], k: int) -> float:
        total_quality = 0
        min_cost = sys.maxsize
        heap = []
        workers = sorted(zip(wage, quality), key=lambda x: x[0] / x[1])

        for cost, q in workers:
            total_quality += q
            heapq.heappush(heap, -q)

            if len(heap) > k:
                total_quality -= -heapq.heappop(heap)

            if len(heap) == k:
                min_cost = min(min_cost, total_quality * cost / q)

        return min_cost
