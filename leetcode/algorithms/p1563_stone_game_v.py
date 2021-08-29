from typing import List


class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefix_sum = [i for i in stoneValue]

        for i in range(n - 1, -1, -1):
            prefix_sum[i] += prefix_sum[i + 1] if i + 1 < n else 0

        return self._dfs(0, n - 1, prefix_sum, {})

    def _dfs(self, start, end, prefix_sum, memo):
        if start == end:
            return 0

        if (start, end) in memo:
            return memo[(start, end)]

        max_score = 0

        for i in range(start, end):
            left_start, left_end = start, i
            right_start, right_end = i + 1, end
            left_sum = prefix_sum[start] - prefix_sum[i + 1]
            right_sum = prefix_sum[i + 1] - (prefix_sum[end + 1] if end + 1 < len(prefix_sum) else 0)
            score = 0

            if 2 * min(left_sum, right_sum) <= max_score:
                continue
            elif left_sum > right_sum:
                score = right_sum + self._dfs(right_start, right_end, prefix_sum, memo)
            elif right_sum > left_sum:
                score = left_sum + self._dfs(left_start, left_end, prefix_sum, memo)
            else:
                left_score = left_sum + self._dfs(left_start, left_end, prefix_sum, memo)
                right_score = right_sum + self._dfs(right_start, right_end, prefix_sum, memo)
                score = max(left_score, right_score)

            max_score = max(max_score, score)

        memo[(start, end)] = max_score

        return max_score
