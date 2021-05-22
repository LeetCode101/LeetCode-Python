from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        diff = 0
        result = [0, 0]

        for n in nums:
            diff ^= n

        diff &= -diff

        for n in nums:
            if n & diff == 0:
                result[0] ^= n
            else:
                result[1] ^= n

        return result
