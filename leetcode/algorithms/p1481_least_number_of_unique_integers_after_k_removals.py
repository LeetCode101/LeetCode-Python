import collections
import heapq
from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = collections.Counter(arr)
        heap = [(count, n) for n, count in counter.items()]
        heapq.heapify(heap)

        while k > 0:
            count, n = heap[0]

            if count > k:
                break

            k -= count
            heapq.heappop(heap)

        return len(heap)
