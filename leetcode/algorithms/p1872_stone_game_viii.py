from typing import List


class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        prefix_sum = [n for n in stones]

        for i in range(1, len(prefix_sum)):
            prefix_sum[i] += prefix_sum[i - 1]

        result = prefix_sum[-1]

        for i in range(len(prefix_sum) - 2, 0, -1):
            result = max(result, prefix_sum[i] - result)

        return result
