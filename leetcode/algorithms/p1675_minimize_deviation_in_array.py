import heapq
from typing import List


class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = list(set(-(x * 2 if x & 1 else x) for x in nums))
        heapq.heapify(heap)
        max_value, min_value = -heap[0], -max(heap)
        result = max_value - min_value

        while heap[0] & 1 == 0:
            x = heapq.heappop(heap) // 2
            heapq.heappush(heap, x)
            max_value, min_value = -heap[0], min(min_value, -x)
            result = min(result, max_value - min_value)

        return result
