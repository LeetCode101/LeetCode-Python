from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[1, 1] for _ in range(n)]
        max_length = 1

        for i in range(1, n):
            if arr[i - 1] < arr[i]:
                dp[i][0] = max(dp[i - 1][1] + 1, 1)
                max_length = max(max_length, dp[i][0])
            elif arr[i - 1] > arr[i]:
                dp[i][1] = max(dp[i - 1][0] + 1, 1)
                max_length = max(max_length, dp[i][1])

        return max_length
