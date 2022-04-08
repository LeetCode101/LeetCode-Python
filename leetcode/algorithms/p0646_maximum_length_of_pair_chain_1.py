from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        sorted_pairs = sorted(pairs, key=lambda x: x[1])
        dp = [1] * n

        for i in range(n):
            for j in range(i + 1, n):
                if sorted_pairs[j][0] > sorted_pairs[i][1]:
                    dp[j] = max(dp[j], dp[i] + 1)

        return max(dp)
