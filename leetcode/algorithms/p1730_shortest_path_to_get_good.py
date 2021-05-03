from collections import deque
from typing import List


class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        if not grid:
            return -1

        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        queue = deque([self._find_start_point(grid, m, n)])

        while queue:
            row, column, distance = queue.popleft()
            visited[row][column] = True

            if grid[row][column] == '#':
                return distance

            for direction in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                next_row = row + direction[0]
                next_column = column + direction[1]

                if next_row < 0 or next_row >= m \
                        or next_column < 0 \
                        or next_column >= n \
                        or grid[next_row][next_column] == 'X' \
                        or visited[next_row][next_column]:
                    continue

                queue.append((next_row, next_column, distance + 1))
                visited[next_row][next_column] = True

        return -1

    def _find_start_point(self, grid, m, n):
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '*':
                    return i, j, 0
