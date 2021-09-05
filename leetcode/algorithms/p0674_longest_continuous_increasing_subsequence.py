from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n

        for i in range(n):
            prev_max = dp[i - 1] if i - 1 >= 0 and nums[i - 1] < nums[i] else 0
            dp[i] = 1 + prev_max

        return max(dp)
