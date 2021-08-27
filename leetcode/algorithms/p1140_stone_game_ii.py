from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        prefix_sum = [n for n in piles]
        memo = [[0] * len(piles) for _ in range(len(piles))]

        for i in range(len(piles) - 2, -1, -1):
            prefix_sum[i] += prefix_sum[i + 1]

        return self._dfs(prefix_sum, 1, 0, memo)

    def _dfs(self, prefix_sum, m, i, memo):
        if i + 2 * m >= len(prefix_sum):
            return prefix_sum[i]

        if memo[i][m] > 0:
            return memo[i][m]

        result = 0

        for j in range(1, 2 * m + 1):
            take = prefix_sum[i] - prefix_sum[i + j]
            result = max(result, take + prefix_sum[i + j] -
                         self._dfs(prefix_sum, max(j, m), i + j, memo))

        memo[i][m] = result

        return result
