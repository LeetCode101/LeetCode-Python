from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            score, jump = questions[i]
            dp[i] = max(dp[i + 1], score + dp[min(jump + i + 1, n)])

        return dp[0]
