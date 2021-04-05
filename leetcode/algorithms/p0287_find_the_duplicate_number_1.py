import collections
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)

        for key, value in counts.items():
            if value > 1:
                return key
