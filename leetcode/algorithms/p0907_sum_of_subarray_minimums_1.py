from typing import List


# Time Limit Exceeded!
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = arr[i]

            for j in range(i + 1, n):
                dp[i][j] = min(dp[i][j - 1], arr[j])

        return sum(map(sum, dp)) % (pow(10, 9) + 7)
