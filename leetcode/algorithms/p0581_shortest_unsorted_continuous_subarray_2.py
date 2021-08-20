from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        prev = nums[0]
        end = 0

        for i, n in enumerate(nums):
            if n < prev:
                end = i
            else:
                prev = n

        start = len(nums) - 1
        prev = nums[start]

        for i in range(len(nums) - 1, -1, -1):
            if prev < nums[i]:
                start = i
            else:
                prev = nums[i]

        return end - start + 1 if end != 0 else 0
