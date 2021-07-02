import sys
from typing import List


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [-sys.maxsize] * n
        dp[-1] = nums[-1]
        max_score = dp[-1]

        for i in range(n - 1, -1, -1):
            dp[i] = nums[i] + max(dp[i + 1:i + k + 1], default=0)
            max_score = max(max_score, dp[i])

        return max_score
