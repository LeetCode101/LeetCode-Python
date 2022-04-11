import heapq
from typing import List


class Solution:
    def maxPerformance(self, n: int, speed: List[int],
                       efficiency: List[int], k: int) -> int:
        mod = 1000000007
        max_performance = 0
        engineers = sorted(zip(efficiency, speed), reverse=True)
        heap = []
        speed_sum = 0

        for e, s in engineers:
            speed_sum += s
            heapq.heappush(heap, s)

            if len(heap) > k:
                speed_sum -= heapq.heappop(heap)

            max_performance = max(max_performance, speed_sum * e)

        return max_performance % mod
