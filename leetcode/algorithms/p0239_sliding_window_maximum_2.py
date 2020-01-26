from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        result = []

        for i, value in enumerate(nums):
            if i >= k and queue[0] <= i - k:
                queue.popleft()

            while queue and nums[queue[-1]] <= value:
                queue.pop()

            queue.append(i)

            if i >= k - 1:
                result.append(nums[queue[0]])

        return result
