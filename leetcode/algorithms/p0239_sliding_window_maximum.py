from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = [(-nums[i], i) for i in range(k)]
        heapify(heap)
        result = [-heap[0][0]] if heap else []

        for i in range(1, len(nums) - k + 1):
            while heap and heap[0][1] < i:
                heappop(heap)

            heappush(heap, (-nums[i + k - 1], i + k - 1))

            result.append(-heap[0][0])

        return result
