from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        sorted_nums = sorted(nums)

        for i in range(1, len(dp)):
            for n in sorted_nums:
                if i - n >= 0:
                    dp[i] += dp[i - n]
                else:
                    break

        return dp[target]
