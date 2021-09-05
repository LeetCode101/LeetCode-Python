import sys
from typing import List


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0] * n for _ in range(n)]

        return self._dfs(dp, arr, 0, n - 1)

    def _dfs(self, dp, arr, left, right):
        if dp[left][right] != 0:
            return dp[left][right]

        if left == right:
            return 0

        smallest = sys.maxsize

        for i in range(left, right):
            left_max = max(arr[left: i + 1])
            right_max = max(arr[i + 1: right + 1])
            left_sum = self._dfs(dp, arr, left, i)
            right_sum = self._dfs(dp, arr, i + 1, right)
            current_sum = left_max * right_max + left_sum + right_sum
            smallest = min(smallest, current_sum)

        dp[left][right] = smallest

        return smallest
