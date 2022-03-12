import heapq
from typing import List


# Time Limit Exceeded!
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        heap = [-x for x in inventory]
        heapq.heapify(heap)
        max_profit = 0

        for _ in range(orders):
            if not heap:
                break

            top = -heapq.heappop(heap)
            max_profit = (max_profit + top) % 1000000007

            if top > 1:
                heapq.heappush(heap, -(top - 1))

        return max_profit
