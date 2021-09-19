from typing import List


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        low, high = 1, k + 1
        result = []

        for i in range(k + 1):
            if i & 1 == 0:
                result.append(low)
                low += 1
            else:
                result.append(high)
                high -= 1

        for i in range(k + 1, n):
            result.append(i + 1)

        return result
