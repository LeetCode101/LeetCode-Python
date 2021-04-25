from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        if target < -total or target > total:
            return 0

        dp = [[0] * (2 * total + 1) for _ in range(len(nums) + 1)]
        dp[0][total] = 1

        for i in range(1, len(nums) + 1):
            for j in range(2 * total + 1):
                if j + nums[i - 1] < 2 * total + 1:
                    dp[i][j] += dp[i - 1][j + nums[i - 1]]

                if j - nums[i - 1] >= 0:
                    dp[i][j] += dp[i - 1][j - nums[i - 1]]

        return dp[len(nums)][total + target]
