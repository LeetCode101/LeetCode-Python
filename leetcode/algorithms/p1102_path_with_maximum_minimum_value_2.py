from typing import List


class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        roots = [i for i in range(m * n)]
        direction = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        visited = [[False] * n for _ in range(m)]

        points = [(x, y) for x in range(m) for y in range(n)]
        points.sort(key=lambda x: grid[x[0]][x[1]], reverse=True)

        for row, column in points:
            visited[row][column] = True

            for dx, dy in direction:
                next_row, next_column = row + dx, column + dy

                if 0 <= next_row < m and 0 <= next_column < n \
                        and visited[next_row][next_column]:
                    self._union(roots, row * n + column,
                                next_row * n + next_column)

            if self._find_root(roots, 0) == \
                    self._find_root(roots, m * n - 1):
                return grid[row][column]

        return -1

    def _find_root(self, roots, x):
        while roots[x] != x:
            roots[x] = roots[roots[x]]
            x = roots[x]

        return roots[x]

    def _union(self, roots, x, y):
        root_x, root_y = self._find_root(roots, x), \
                         self._find_root(roots, y)

        if root_x != root_y:
            roots[root_x] = root_y
