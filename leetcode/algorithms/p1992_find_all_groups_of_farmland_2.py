from typing import List


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])
        result = []
        visited = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if land[i][j] == 0 or visited[i][j]:
                    continue

                top_left_row, top_left_column = i, j
                bottom_right_row, bottom_right_column = \
                    self._dfs(land, i, j, visited)

                result.append([top_left_row, top_left_column,
                               bottom_right_row, bottom_right_column])

        return result

    def _dfs(self, land, row, column, visited):
        m, n = len(land), len(land[0])

        if row < 0 or row >= m \
                or column < 0 or column >= n \
                or land[row][column] == 0 or visited[row][column]:
            return -1, -1

        visited[row][column] = True
        max_bottom_right_row = row
        max_bottom_right_column = column

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_row = row + dx
            next_column = column + dy
            current_bottom_right_row, current_bottom_right_column = \
                self._dfs(land, next_row, next_column, visited)
            max_bottom_right_row = max(
                max_bottom_right_row, current_bottom_right_row)
            max_bottom_right_column = max(
                max_bottom_right_column, current_bottom_right_column)

        return max_bottom_right_row, max_bottom_right_column
