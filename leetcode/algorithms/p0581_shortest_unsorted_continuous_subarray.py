from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_numbers = sorted(nums)
        start, end = 0, len(nums) - 1

        while start < len(nums) and sorted_numbers[start] == nums[start]:
            start += 1

        while end >= 0 and sorted_numbers[end] == nums[end]:
            end -= 1

        return end - start + 1 if start != len(nums) and end != -1 else 0
