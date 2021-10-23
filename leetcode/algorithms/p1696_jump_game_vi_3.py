from collections import deque
from typing import List


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        queue = deque([0])

        for i in range(1, n):
            if queue[0] < i - k:
                queue.popleft()

            dp[i] = nums[i] + dp[queue[0]]

            while queue and dp[queue[-1]] <= dp[i]:
                queue.pop()

            queue.append(i)

        return dp[-1]
