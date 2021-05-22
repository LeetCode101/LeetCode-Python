from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        mask = 0
        result = [0, 0]

        for n in nums:
            mask ^= n

        mask &= -mask

        for n in nums:
            if n & mask == 0:
                result[0] ^= n
            else:
                result[1] ^= n

        return result
