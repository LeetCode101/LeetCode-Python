from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack, result = [], [-1] * len(nums)

        for i in range(len(nums) * 2):
            n = nums[i % len(nums)]

            while stack and nums[stack[-1]] < n:
                result[stack.pop()] = n

            if i < len(nums):
                stack.append(i)

        return result
