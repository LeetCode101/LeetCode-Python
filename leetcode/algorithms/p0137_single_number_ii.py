from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for i in range(32):
            sum = 0

            for num in nums:
                sum += ((num >> i) & 1)

            if sum % 3 == 1:
                if i == 31:
                    result -= (1 << 31)
                else:
                    result |= 1 << i

        return result
