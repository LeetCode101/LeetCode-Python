from typing import List


# Time Limit Exceeded!
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if arr[i] - arr[j] == difference:
                    dp[i] = dp[j] + 1

                    break

        return max(dp)
