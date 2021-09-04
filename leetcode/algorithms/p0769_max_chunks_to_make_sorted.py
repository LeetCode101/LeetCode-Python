from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        count = 0

        for i, n in enumerate(arr):
            if stack and stack[-1] < n:
                prev_max = stack.pop()
                prev_sorted_array_size = prev_max + 1

                if not stack and prev_sorted_array_size == i:
                    count += 1

            if not stack:
                stack.append(n)

        return count + (1 if len(stack) > 0 else 0)
