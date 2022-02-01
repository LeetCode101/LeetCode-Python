import collections
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = collections.deque([])
        m, n = len(grid), len(grid[0])
        fresh_count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1

        minutes = 0
        visited = [[False] * n for _ in range(m)]

        while queue:
            size = len(queue)
            affected = False

            for _ in range(size):
                row, column = queue.popleft()
                visited[row][column] = True

                for dx, dy in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                    next_row = row + dx
                    next_column = column + dy

                    if 0 <= next_row < m and 0 <= next_column < n \
                            and not visited[next_row][next_column] \
                            and grid[next_row][next_column] == 1:
                        affected = True
                        fresh_count -= 1
                        visited[next_row][next_column] = True
                        queue.append((next_row, next_column))

            if affected:
                minutes += 1

        return minutes if fresh_count == 0 else -1
