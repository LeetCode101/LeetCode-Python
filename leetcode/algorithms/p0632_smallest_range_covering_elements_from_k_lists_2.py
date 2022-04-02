import heapq
import sys
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = [(x[0], i, 0) for i, x in enumerate(nums)]
        heapq.heapify(heap)
        result = [-sys.maxsize, sys.maxsize]
        right = max(x[0] for x in nums)

        while heap:
            left, i, j = heapq.heappop(heap)

            if right - left < result[1] - result[0]:
                result = [left, right]

            if j + 1 == len(nums[i]):
                return result

            value = nums[i][j + 1]
            right = max(right, value)
            heapq.heappush(heap, (value, i, j + 1))
