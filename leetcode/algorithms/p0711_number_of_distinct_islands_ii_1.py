from typing import List


class Solution:
    def numDistinctIslands2(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        paths = set()
        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    path = []

                    self._dfs(i, j, grid, visited, path)
                    path = self._normalize(path)

                    if self._is_all_path_variation_unique(path, paths):
                        paths.add(tuple(path))

        return len(paths)

    def _dfs(self, row, column, grid, visited, path):
        m, n = len(grid), len(grid[0])

        if row < 0 or row >= m or column < 0 or column >= n \
                or grid[row][column] != 1 or visited[row][column]:
            return

        visited[row][column] = True
        path.append((row, column))

        for direction in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            self._dfs(row + direction[0], column + direction[1],
                      grid, visited, path)

    def _normalize(self, path):
        sorted_path = sorted(path)

        return [(x - sorted_path[0][0], y - sorted_path[0][1])
                for x, y in sorted_path]

    def _is_all_path_variation_unique(self, path, paths):
        if tuple(path) in paths or not self._is_rotation_unique(path, paths):
            return False

        horizontal_path = self._normalize([(-x, y) for x, y in path])

        if tuple(horizontal_path) in paths \
                or not self._is_rotation_unique(horizontal_path, paths):
            return False

        vertical_path = self._normalize([(x, -y) for x, y in path])

        if tuple(vertical_path) in paths \
                or not self._is_rotation_unique(vertical_path, paths):
            return False

        return True

    def _is_rotation_unique(self, path, paths):
        for i in range(3):
            path = self._normalize([(y, -x) for x, y in path])

            if tuple(path) in paths:
                return False

        return True
