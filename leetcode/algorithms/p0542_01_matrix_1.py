import sys
from typing import List


# Time Limit Exceeded!
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return []

        m, n = len(mat), len(mat[0])
        distances = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    distances[i][j] = sys.maxsize

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    self._dfs(mat, i, j, distances, 0)

        return distances

    def _dfs(self, mat, row, column, distances, distance):
        m, n = len(mat), len(mat[0])

        distances[row][column] = distance

        for direction in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            next_row = row + direction[0]
            next_column = column + direction[1]

            if next_row < 0 or next_row >= m \
                    or next_column < 0 or next_column >= n \
                    or distances[next_row][next_column] <= distance:
                continue

            self._dfs(mat, next_row, next_column, distances, distance + 1)
