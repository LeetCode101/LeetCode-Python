import heapq
from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heap = [n for n in nums]
        heapq.heapify(heap)

        for _ in range(k):
            heapq.heappush(heap, -heapq.heappop(heap))

        return sum(heap)
