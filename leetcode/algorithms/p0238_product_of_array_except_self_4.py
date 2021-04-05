from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [1] * length
        left = right = 1

        for i in range(length):
            result[i] *= left
            result[length - i - 1] *= right
            left *= nums[i]
            right *= nums[length - i - 1]

        return result
