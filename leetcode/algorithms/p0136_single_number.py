from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        number = nums[0]

        for i in range(1, len(nums)):
            number ^= nums[i]

        return number
