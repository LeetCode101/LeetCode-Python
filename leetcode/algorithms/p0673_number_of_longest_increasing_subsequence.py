from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        counts = [0] * n

        for i in range(n):
            max_length = 1
            max_count = 1

            for j in range(i):
                if nums[j] >= nums[i]:
                    continue

                if dp[j] + 1 == max_length:
                    max_count += counts[j]
                elif dp[j] + 1 > max_length:
                    max_count = counts[j]
                    max_length = dp[j] + 1

            dp[i] = max_length
            counts[i] = max_count

        longest = max(dp)
        count = 0

        for i in range(n):
            if dp[i] == longest:
                count += counts[i]

        return count
