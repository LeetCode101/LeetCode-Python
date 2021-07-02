import sys
from typing import List


# Time Limit Exceeded!
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [-sys.maxsize] * n
        dp[0] = nums[0]

        for i in range(1, n):
            for j in range(max(i - k, 0), i):
                dp[i] = max(dp[i], dp[j] + nums[i])

        return dp[-1]
