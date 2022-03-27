from typing import List


class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        low, high = min(sweetness), sum(sweetness)

        while low < high:
            middle = low + (high - low) // 2 + 1
            count = self._count(sweetness, middle)

            if count < k + 1:
                high = middle - 1
            else:
                low = middle

        return low

    def _count(self, sweetness, sweet):
        sum_so_far = 0
        count = 0

        for x in sweetness:
            sum_so_far += x

            if sum_so_far >= sweet:
                count += 1
                sum_so_far = 0

        return count
