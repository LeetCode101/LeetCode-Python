from typing import List


class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0, 0] for _ in range(n)]
        dp[0] = [nums[0], nums[0] * nums[0]]
        max_sum = dp[0][1]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0] + nums[i], nums[i])
            dp[i][1] = max(max(dp[i - 1][0] + nums[i] * nums[i],
                               dp[i - 1][1] + nums[i]), nums[i] * nums[i])
            max_sum = max(max_sum, dp[i][1])

        return max_sum
