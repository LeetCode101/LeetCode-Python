import sys
from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1

        largest = -sys.maxsize
        second_largest = -sys.maxsize
        largest_index = 0

        for i, n in enumerate(nums):
            if n > largest:
                largest, second_largest = n, largest
                largest_index = i
            elif n > second_largest:
                second_largest = n

        return largest_index if largest >= 2 * second_largest else -1
