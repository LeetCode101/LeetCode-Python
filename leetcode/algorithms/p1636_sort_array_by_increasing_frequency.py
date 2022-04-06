import collections
import heapq
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = collections.Counter(nums)
        result = []
        heap = [(count, -n) for n, count in counter.items()]
        heapq.heapify(heap)

        while heap:
            count, n = heapq.heappop(heap)
            result.extend([-n] * count)

        return result
