import sys
from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1

        largest = -sys.maxsize
        largest_index = 0

        for i, n in enumerate(nums):
            if largest < n:
                largest = n
                largest_index = i

        for n in nums:
            if n != largest and largest < 2 * n:
                return -1

        return largest_index
