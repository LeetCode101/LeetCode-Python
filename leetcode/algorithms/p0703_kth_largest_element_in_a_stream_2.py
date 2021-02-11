from heapq import heappush, heappop, heapify
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [n for n in nums]

        heapify(self.heap)

        while len(self.heap) > self.k:
            heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) == self.k and self.heap[0] > val:
            return self.heap[0]

        heappush(self.heap, val)

        if len(self.heap) > self.k:
            heappop(self.heap)

        return self.heap[0]
