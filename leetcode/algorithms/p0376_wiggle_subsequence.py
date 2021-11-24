from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[1, 1] for _ in range(n)]
        max_length = 0

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i][0] = max(dp[i][0], dp[j][1] + 1)
                elif nums[i] < nums[j]:
                    dp[i][1] = max(dp[i][1], dp[j][0] + 1)

            max_length = max(dp[i][0], dp[i][1])

        return max_length
