from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(nums))]
        dp[0] = [nums[0], nums[0]]

        for i in range(1, len(nums)):
            value = nums[i]

            dp[i][0] = max(dp[i - 1][0] * value, dp[i - 1][1] * value, value)
            dp[i][1] = min(dp[i - 1][0] * value, dp[i - 1][1] * value, value)

        return max(x[0] for x in dp)
