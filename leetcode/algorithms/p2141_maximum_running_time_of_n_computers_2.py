import heapq
from typing import List


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        total_energy = sum(batteries)
        heap = [-x for x in batteries]
        heapq.heapify(heap)

        while -heap[0] > total_energy // n:
            total_energy -= -heapq.heappop(heap)
            n -= 1

        return total_energy // n
