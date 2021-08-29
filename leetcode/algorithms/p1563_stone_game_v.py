import sys
from typing import List


class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefix_sum = [i for i in stoneValue]

        for i in range(n - 1, -1, -1):
            prefix_sum[i] += prefix_sum[i + 1] if i + 1 < n else 0

        return self._dfs(0, n - 1, prefix_sum, {})

    def _dfs(self, start, end, prefix_sum, memo):
        if (start, end) in memo:
            return memo[(start, end)]

        if start == end:
            return 0

        max_score = -sys.maxsize

        for i in range(start, end):
            left = [start, i]
            right = [i + 1, end]
            left_sum = prefix_sum[start] - prefix_sum[i + 1]
            right_sum = prefix_sum[i + 1] - (prefix_sum[end + 1] if end + 1 < len(prefix_sum) else 0)

            if i > start and 2 * min(left_sum, right_sum) < max_score:
                continue
            if left_sum > right_sum:
                value = right_sum + self._dfs(right[0], right[1], prefix_sum, memo)
            elif right_sum > left_sum:
                value = left_sum + self._dfs(left[0], left[1], prefix_sum, memo)
            else:
                value = max(left_sum + self._dfs(left[0], left[1], prefix_sum, memo), right_sum + self._dfs(right[0], right[1], prefix_sum, memo))

            if i > start:
                max_score = max(max_score, value)
            else:
                max_score = value

        memo[(start, end)] = max_score

        return max_score
