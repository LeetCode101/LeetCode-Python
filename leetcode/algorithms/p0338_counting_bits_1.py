from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        return [self._hammingWeight(x) for x in range(num + 1)]

    def _hammingWeight(self, n: int) -> int:
        count = 0

        while n > 0:
            n = n & (n - 1)

            count += 1

        return count
