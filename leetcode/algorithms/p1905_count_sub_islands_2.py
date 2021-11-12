import collections
from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) \
            -> int:
        count = 0
        m, n = len(grid1), len(grid1[0])
        visited = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and not visited[i][j]:
                    if self._bfs(grid1, grid2, visited, i, j):
                        count += 1

        return count

    def _bfs(self, grid1, grid2, visited, x, y):
        m, n = len(grid1), len(grid1[0])
        visited[x][y] = True
        is_sub_island = True

        if grid1[x][y] == 0:
            is_sub_island = False

        queue = collections.deque([(x, y)])

        while queue:
            row, column = queue.popleft()

            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                next_row = row + dx
                next_column = column + dy

                if next_row < 0 or next_row >= m \
                        or next_column < 0 or next_column >= n \
                        or grid2[next_row][next_column] == 0 \
                        or visited[next_row][next_column]:
                    continue

                if grid1[next_row][next_column] == 0:
                    is_sub_island = False

                queue.append((next_row, next_column))
                visited[next_row][next_column] = True

        return is_sub_island
