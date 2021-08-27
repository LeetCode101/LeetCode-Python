import sys
from typing import List


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [-sys.maxsize] * n

        for i in range(n - 1, -1, -1):
            take = 0

            for j in range(i, min(n, i + 3)):
                take += stoneValue[j]
                dp[i] = max(dp[i], take - dp[j + 1] if j + 1 < n else take)

        if dp[0] > 0:
            return 'Alice'
        elif dp[0] < 0:
            return 'Bob'
        else:
            return 'Tie'
