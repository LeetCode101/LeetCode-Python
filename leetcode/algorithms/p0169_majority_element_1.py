from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        number_mapping = {}

        for n in nums:
            number_mapping[n] = number_mapping.get(n, 0) + 1

        for key, value in number_mapping.items():
            if value >= len(nums) / 2:
                return key
