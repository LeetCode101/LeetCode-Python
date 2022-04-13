import sys
from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        s3 = -sys.maxsize
        stack = []

        for i in range(len(nums) - 1, -1, -1):
            n = nums[i]

            if n < s3:
                return True

            while stack and n > stack[-1]:
                s3 = stack[-1]
                stack.pop()

            stack.append(n)

        return False
