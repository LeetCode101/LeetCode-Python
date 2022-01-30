import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heap = [(0, 0, 0)]
        heapq.heapify(heap)
        m, n = len(heights), len(heights[0])
        min_effort = 0
        visited = [[set() for _ in range(n)] for _ in range(m)]
        directions = [(0, -1, 'L'), (-1, 0, 'U'), (0, 1, 'R'), (1, 0, 'D')]
        opposite_direction = {
            'L': 'R',
            'R': 'L',
            'U': 'D',
            'D': 'U'
        }

        while heap:
            effort, row, column = heapq.heappop(heap)
            min_effort = max(min_effort, effort)

            if row == m - 1 and column == n - 1:
                break

            for dx, dy, direction in directions:
                next_row = row + dx
                next_column = column + dy

                if 0 <= next_row < m and 0 <= next_column < n \
                        and opposite_direction[direction] \
                        not in visited[next_row][next_column]:
                    effort = abs(heights[row][column] -
                                 heights[next_row][next_column])
                    heapq.heappush(heap, (effort, next_row, next_column))
                    visited[next_row][next_column].add(
                        opposite_direction[direction])

        return min_effort
