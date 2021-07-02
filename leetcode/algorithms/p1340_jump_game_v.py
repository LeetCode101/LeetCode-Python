from typing import List


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [0] * n
        max_jumps = 0

        for i in range(n):
            max_jumps = max(max_jumps, self._dfs(arr, n, d, i, dp))

        return max_jumps

    def _dfs(self, arr, n, d, start, dp):
        if dp[start] != 0:
            return dp[start]

        max_jumps = 1
        j = start + 1

        while j <= min(start + d, n - 1) and arr[j] < arr[start]:
            max_jumps = max(max_jumps, 1 + self._dfs(arr, n, d, j, dp))
            j += 1

        j = start - 1

        while j >= max(start - d, 0) and arr[j] < arr[start]:
            max_jumps = max(max_jumps, 1 + self._dfs(arr, n, d, j, dp))
            j -= 1

        dp[start] = max_jumps

        return dp[start]
