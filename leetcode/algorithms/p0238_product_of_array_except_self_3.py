from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [1] * length
        left_products = [1] * length
        right_products = [1] * length

        for i in range(length):
            left_products[i] = nums[i] if i == 0 else \
                nums[i] * left_products[i - 1]
            right_products[i] = nums[length - i - 1] if i == 0 else \
                nums[length - i - 1] * right_products[i - 1]

        for i in range(length):
            if i == 0:
                result[i] = right_products[length - i - 2]
            elif i == length - 1:
                result[i] = left_products[i - 1]
            else:
                result[i] = left_products[i - 1] * \
                            right_products[length - i - 2]

        return result
