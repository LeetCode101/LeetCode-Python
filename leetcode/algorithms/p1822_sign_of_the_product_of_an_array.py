from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negative = 0

        for n in nums:
            if n == 0:
                return 0
            elif n < 0:
                negative += 1

        return -1 if negative & 1 == 1 else 1
