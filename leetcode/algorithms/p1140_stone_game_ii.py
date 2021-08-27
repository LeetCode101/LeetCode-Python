from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        prefix_sum = [n for n in piles]
        memo = [[0] * len(piles) for _ in range(len(piles))]

        for i in range(len(piles) - 2, -1, -1):
            prefix_sum[i] += prefix_sum[i + 1]

        return self._dfs(prefix_sum, 1, 0, memo)

    def _dfs(self, prefix_sum, m, p, memo):
        if p + 2 * m >= len(prefix_sum):
            return prefix_sum[p]

        if memo[p][m] > 0:
            return memo[p][m]

        result = 0

        for i in range(1, 2 * m + 1):
            take = prefix_sum[p] - prefix_sum[p + i]
            result = max(result, take + prefix_sum[p + i] -
                         self._dfs(prefix_sum, max(i, m), p + i, memo))

        memo[p][m] = result

        return result
