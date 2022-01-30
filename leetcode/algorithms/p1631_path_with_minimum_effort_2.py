import heapq
import sys
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heap = [(0, 0, 0)]
        heapq.heapify(heap)
        m, n = len(heights), len(heights[0])
        min_effort = 0
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        efforts = [[sys.maxsize] * n for _ in range(m)]

        while heap:
            effort, row, column = heapq.heappop(heap)
            min_effort = max(min_effort, effort)

            if row == m - 1 and column == n - 1:
                break

            for dx, dy in directions:
                next_row = row + dx
                next_column = column + dy

                if 0 <= next_row < m and 0 <= next_column < n:
                    effort = abs(heights[row][column] -
                                 heights[next_row][next_column])

                    if efforts[next_row][next_column] > effort:
                        efforts[next_row][next_column] = effort
                        heapq.heappush(heap, (effort, next_row, next_column))

        return min_effort
