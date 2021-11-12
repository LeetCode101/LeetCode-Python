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
                    if self._dfs(grid1, grid2, visited, i, j):
                        count += 1

        return count

    def _dfs(self, grid1, grid2, visited, x, y):
        m, n = len(grid1), len(grid1[0])
        visited[x][y] = True
        is_sub_island = True

        if grid1[x][y] == 0:
            is_sub_island = False

        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            next_row = x + dx
            next_column = y + dy

            if next_row < 0 or next_row >= m \
                    or next_column < 0 or next_column >= n \
                    or grid2[next_row][next_column] == 0 \
                    or visited[next_row][next_column]:
                continue

            if grid1[next_row][next_column] == 0:
                is_sub_island = False

            is_sub_island = self._dfs(grid1, grid2, visited,
                                      next_row, next_column) and is_sub_island

        return is_sub_island
