import heapq
from typing import List


class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        heap = [(-grid[0][0], 0, 0)]
        heapq.heapify(heap)
        m, n = len(grid), len(grid[0])
        max_score = grid[0][0]
        visited = [[False] * n for _ in range(m)]

        while heap:
            score, row, column = heapq.heappop(heap)
            max_score = min(max_score, -score)
            visited[row][column] = True

            if row == m - 1 and column == n - 1:
                break

            for dx, dy in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                next_row = row + dx
                next_column = column + dy

                if 0 <= next_row < m and 0 <= next_column < n \
                        and not visited[next_row][next_column]:
                    heapq.heappush(heap, (-grid[next_row][next_column],
                                          next_row, next_column))

        return max_score
