import collections
from typing import List


# Time Limit Exceeded!
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) \
            -> int:
        islands1 = self._get_islands(grid1)
        islands2 = self._get_islands(grid2)
        count = 0

        for island in islands2:
            for full_island in islands1:
                if island.issubset(full_island):
                    count += 1

        return count

    def _get_islands(self, grid):
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        islands = []

        for i in range(m):
            for j in range(n):
                if visited[i][j] or grid[i][j] == 0:
                    continue

                island = set()
                queue = collections.deque([(i, j)])
                visited[i][j] = True

                while queue:
                    row, column = queue.popleft()
                    island.add((row, column))

                    for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                        next_row = row + dx
                        next_column = column + dy

                        if next_row < 0 or next_row >= m \
                                or next_column < 0 or next_column >= n \
                                or grid[next_row][next_column] == 0 \
                                or visited[next_row][next_column]:
                            continue

                        queue.append((next_row, next_column))
                        visited[next_row][next_column] = True

                islands.append(island)

        return islands
