from typing import List


# Time Limit Exceeded!
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return [self._product(i, nums) for i in range(len(nums))]

    def _product(self, i, nums: List[int]) -> int:
        product = 1

        for j, n in enumerate(nums):
            if j != i:
                product *= n

        return product
