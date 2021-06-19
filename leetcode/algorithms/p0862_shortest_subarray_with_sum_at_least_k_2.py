import sys
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        stack = [(0, -1)]
        sum_so_far = 0
        min_length = sys.maxsize

        for i, n in enumerate(nums):
            sum_so_far += n

            while stack and stack[-1][0] >= sum_so_far:
                stack.pop()

            j = self._find_left(stack, sum_so_far - k)

            if j > 0:
                min_length = min(min_length, i - stack[j - 1][1])

            stack.append((sum_so_far, i))

        return min_length < sys.maxsize and min_length or -1

    def _find_left(self, stack, target):
        low, high = 0, len(stack)

        while low < high:
            middle = low + (high - low) // 2

            if stack[middle][0] <= target:
                low = middle + 1
            else:
                high = middle

        return low
