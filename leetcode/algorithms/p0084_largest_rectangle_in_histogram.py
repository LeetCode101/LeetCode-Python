from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        length = len(heights)
        i = 0

        while i <= length:
            current_height = 0 if i == length else heights[i]

            if not stack or current_height >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                top = stack.pop()
                width = i if not stack else i - 1 - stack[-1]
                current_area = heights[top] * width
                max_area = max(max_area, current_area)

        return max_area
