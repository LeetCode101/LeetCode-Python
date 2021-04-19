import collections
from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        max_area = 0
        island_index = 0
        areas = collections.Counter()
        visited = [[False for _ in range(n)] for _ in range(m)]
        islands = [[-1 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    island_index += 1

                    self._dfs(grid, i, j, visited, island_index,
                              areas, islands)

                    max_area = max(max_area, areas[island_index])

        return max(max_area, self._get_max_area(m, n, grid, areas, islands))

    def _dfs(self, grid, row, column, visited, island_index, areas, islands):
        m, n = len(grid), len(grid[0])

        if row < 0 or row >= m or column < 0 or column >= n \
                or grid[row][column] != 1 or visited[row][column]:
            return

        visited[row][column] = True
        areas[island_index] += 1
        islands[row][column] = island_index

        for direction in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            self._dfs(grid, row + direction[0],
                      column + direction[1], visited,
                      island_index, areas, islands)

    def _get_max_area(self, m, n, grid, areas, islands):
        max_area = 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    continue

                area = 1
                neighbour_islands = set()

                for direction in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                    next_row = i + direction[0]
                    next_column = j + direction[1]

                    if next_row < 0 or next_row >= m \
                            or next_column < 0 \
                            or next_column >= n:
                        continue

                    neighbour_islands.add(islands[next_row][next_column])

                for island in neighbour_islands:
                    area += areas[island]

                max_area = max(max_area, area)

        return max_area
