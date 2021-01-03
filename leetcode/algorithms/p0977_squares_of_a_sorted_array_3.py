from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        low, high = 0, len(nums) - 1

        while low <= high:
            left, right = abs(nums[low]), abs(nums[high])

            if left > right:
                result[high - low] = left * left
                low += 1
            else:
                result[high - low] = right * right
                high -= 1

        return result
