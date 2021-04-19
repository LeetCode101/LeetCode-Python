import collections
from typing import List


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])

        max_area = 0
        island_tag = 100
        visited = [[False for _ in range(n)] for _ in range(m)]
        areas = collections.Counter()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 or visited[i][j]:
                    continue

                island_tag += 1
                visited[i][j] = True
                queue = [(i, j)]

                while queue:
                    (row, column) = queue.pop(0)
                    areas[island_tag] += 1
                    max_area = max(max_area, areas[island_tag])
                    grid[row][column] = island_tag

                    for direction in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                        next_row = row + direction[0]
                        next_column = column + direction[1]

                        if next_row < 0 or next_row >= m \
                                or next_column < 0 \
                                or next_column >= n \
                                or grid[next_row][next_column] == 0 \
                                or visited[next_row][next_column]:
                            continue

                        visited[next_row][next_column] = True
                        queue.append((next_row, next_column))

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    continue

                area = 1
                islands = set()

                for direction in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                    next_row = i + direction[0]
                    next_column = j + direction[1]

                    if next_row < 0 or next_row >= m \
                            or next_column < 0 \
                            or next_column >= n:
                        continue

                    islands.add(grid[next_row][next_column])

                for island in islands:
                    area += areas[island]

                max_area = max(max_area, area)

        return max_area
