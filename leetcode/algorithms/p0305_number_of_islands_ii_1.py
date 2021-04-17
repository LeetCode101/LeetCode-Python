from collections import deque
from typing import List


# Time Limit Exceeded!
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) \
            -> List[int]:
        grid = [['0'] * n for _ in range(m)]
        counts = [0] * len(positions)

        for i, position in enumerate(positions):
            row, column = position[0], position[1]
            grid[row][column] = 1
            counts[i] = self._num_islands(grid)

        return counts

    def _num_islands(self, grid: List[List[str]]) -> int:
        count = 0
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    count += 1
                    visited[i][j] = True
                    queue = deque([(i, j)])

                    while queue:
                        cell = queue.popleft()
                        row, column = cell[0], cell[1]

                        for direction in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                            next_row = row + direction[0]
                            next_column = column + direction[1]

                            if next_row < 0 or next_row >= m \
                                    or next_column < 0 \
                                    or next_column >= n \
                                    or grid[next_row][next_column] != 1 \
                                    or visited[next_row][next_column]:
                                continue

                            queue.append((next_row, next_column))
                            visited[next_row][next_column] = True

        return count
