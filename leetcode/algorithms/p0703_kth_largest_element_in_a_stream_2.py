from heapq import heappush, heappop
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []

        for n in nums:
            self.add_to_heap(n)

    def add(self, val: int) -> int:
        if len(self.heap) == self.k and self.heap[0] > val:
            return self.heap[0]

        self.add_to_heap(val)

        return self.heap[0]

    def add_to_heap(self, val: int) -> None:
        heappush(self.heap, val)

        if len(self.heap) > self.k:
            heappop(self.heap)
