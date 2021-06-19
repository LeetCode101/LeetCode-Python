from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        heights = [0] * (n + 1)
        max_area = 0

        for i in range(m):
            for j in range(n):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0

            max_area = max(max_area, self._get_max_area(heights))

        return max_area

    def _get_max_area(self, heights):
        stack = [-1]
        max_area = 0

        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - 1 - stack[-1]
                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area
