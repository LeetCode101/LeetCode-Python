import heapq
from typing import List


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        n = len(nums)
        heap = [(-nums[0], 0)]
        max_score = nums[0]

        for i in range(1, n):
            while heap[0][1] < i - k:
                heapq.heappop(heap)

            max_score = -(-nums[i] + heap[0][0])
            heapq.heappush(heap, (-max_score, i))

        return max_score
