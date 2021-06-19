from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        max_area = 0

        for i in range(m):
            for j in range(n):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0

            max_area = max(max_area, self._get_max_area(heights))

        return max_area

    def _get_max_area(self, heights):
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
