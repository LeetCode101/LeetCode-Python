from collections import deque
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])
        count = 0
        visited = [[False for _ in range(n)] for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == 0 and not visited[i][j]:
                    visited[i][j] = True
                    queue = deque([(i, j)])
                    closed = True

                    while queue:
                        cell = queue.popleft()
                        row, column = cell[0], cell[1]

                        for direction in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                            next_row = row + direction[0]
                            next_column = column + direction[1]

                            if next_row < 0 or next_row >= m \
                                    or next_column < 0 \
                                    or next_column >= n:
                                closed = False

                                continue

                            if visited[next_row][next_column] \
                                    or grid[next_row][next_column] == 1:
                                continue

                            queue.append((next_row, next_column))
                            visited[next_row][next_column] = True

                    if closed:
                        count += 1

        return count
