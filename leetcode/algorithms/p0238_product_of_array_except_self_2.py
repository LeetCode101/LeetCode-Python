from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros = 0

        for n in nums:
            if n == 0:
                zeros += 1
            else:
                product *= n

        if zeros == 1:
            return [0 if n != 0 else product for n in nums]
        elif zeros >= 2:
            return [0] * len(nums)
        else:
            return [product // n for n in nums]
