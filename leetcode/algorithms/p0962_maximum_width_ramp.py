from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        max_length = 0

        for i, n in enumerate(nums):
            if not stack or nums[stack[-1]] > n:
                stack.append(i)

        for i in range(len(nums) - 1, -1, -1):
            n = nums[i]

            while stack and n >= nums[stack[-1]]:
                max_length = max(max_length, i - stack.pop())

        return max_length
