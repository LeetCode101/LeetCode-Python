from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [0] * len(nums)

        for i in range(len(nums)):
            dp[i] = max(
                [dp[j] for j in range(i) if nums[j] < nums[i]], default=0) + 1

        return max(dp)
