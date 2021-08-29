from typing import List


class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefix_sum = [i for i in stoneValue]

        for i in range(1, n):
            prefix_sum[i] += prefix_sum[i - 1]

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
            left_sum = prefix_sum[left_end] - (prefix_sum[left_start - 1]
                                               if left_start - 1 >= 0 else 0)
            right_sum = prefix_sum[right_end] - prefix_sum[right_start - 1]
            score = 0

            if 2 * min(left_sum, right_sum) <= max_score:
                continue
            elif left_sum > right_sum:
                score = right_sum + self._dfs(
                    right_start, right_end, prefix_sum, memo)
            elif right_sum > left_sum:
                score = left_sum + self._dfs(
                    left_start, left_end, prefix_sum, memo)
            else:
                left_score = left_sum + self._dfs(
                    left_start, left_end, prefix_sum, memo)
                right_score = right_sum + self._dfs(
                    right_start, right_end, prefix_sum, memo)
                score = max(left_score, right_score)

            max_score = max(max_score, score)

        memo[(start, end)] = max_score

        return max_score
