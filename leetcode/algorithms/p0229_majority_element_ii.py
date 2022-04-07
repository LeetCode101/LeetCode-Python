import collections
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = collections.Counter(nums)
        result = []

        for n, count in counter.items():
            if count > len(nums) / 3:
                result.append(n)

        return result
