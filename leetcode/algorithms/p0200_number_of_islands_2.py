from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        count = 0
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    count += 1
                    visited[i][j] = True
                    queue = deque([(i, j)])

                    while queue:
                        cell = queue.popleft()
                        row, column = cell[0], cell[1]

                        if row - 1 >= 0 and grid[row - 1][column] == '1' \
                                and not visited[row - 1][column]:
                            queue.append((row - 1, column))
                            visited[row - 1][column] = True

                        if row + 1 <= m - 1 and grid[row + 1][column] == '1' \
                                and not visited[row + 1][column]:
                            queue.append((row + 1, column))
                            visited[row + 1][column] = True

                        if column - 1 >= 0 and grid[row][column - 1] == '1' \
                                and not visited[row][column - 1]:
                            queue.append((row, column - 1))
                            visited[row][column - 1] = True

                        if column + 1 <= n - 1 \
                                and grid[row][column + 1] == '1' \
                                and not visited[row][column + 1]:
                            queue.append((row, column + 1))
                            visited[row][column + 1] = True

        return count
