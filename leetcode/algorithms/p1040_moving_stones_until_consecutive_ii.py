from typing import List


class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        sorted_stones = sorted(stones)
        i, n = 0, len(sorted_stones)
        low = n
        high = max(sorted_stones[-1] - sorted_stones[1] + 1 - (n - 1),
                   sorted_stones[-2] - sorted_stones[0] + 1 - (n - 1))

        for j in range(n):
            while sorted_stones[j] - sorted_stones[i] + 1 > n:
                i += 1

            if j - i + 1 == n - 1 \
                    and sorted_stones[j] - sorted_stones[i] == j - i:
                low = min(low, 2)
            else:
                low = min(low, n - (j - i + 1))

        return [low, high]
