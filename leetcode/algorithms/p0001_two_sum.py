from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {}

        for index, value in enumerate(nums):
            diff = target - value

            if diff in mapping:
                return [mapping[diff], index]
            else:
                mapping[value] = index

        return [-1, -1]
