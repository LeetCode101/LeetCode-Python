from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        disappeared = []

        for n in nums:
            index = abs(n) - 1
            nums[index] = -abs(nums[index])

        for i, n in enumerate(nums):
            if n > 0:
                disappeared.append(i + 1)

        return disappeared
