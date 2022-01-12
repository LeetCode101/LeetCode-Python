from typing import List


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        length = len(nums)

        for i, n in enumerate(nums):
            left = length - i

            while stack and n < stack[-1] and len(stack) + left > k:
                stack.pop()

            if len(stack) < k:
                stack.append(n)

        return stack
