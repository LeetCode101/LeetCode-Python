from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_length = 0

        for x in nums:
            if x - 1 not in nums:
                y = x + 1

                while y in nums:
                    y += 1

                max_length = max(max_length, y - x)

        return max_length
