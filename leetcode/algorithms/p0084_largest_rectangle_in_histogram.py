from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        length = len(heights)
        i = 0

        while i <= length:
            height = 0 if i == length else heights[i]

            if not stack or height >= heights[stack[-1]]:
                stack.append(i)
            else:
                top = stack.pop()
                max_area = max(max_area, heights[top] * (i if not stack else i - 1 - stack[-1]))
                i -= 1

            i += 1

        return max_area
