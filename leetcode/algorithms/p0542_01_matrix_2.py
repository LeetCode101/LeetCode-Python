from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat:
            return []

        m, n = len(mat), len(mat[0])
        visited = [[False] * n for _ in range(m)]
        distances = [[0] * n for _ in range(m)]
        queue = deque([])

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    visited[i][j] = True

        while queue:
            row, column = queue.popleft()

            for direction in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                next_row = row + direction[0]
                next_column = column + direction[1]

                if next_row < 0 or next_row >= m \
                        or next_column < 0 \
                        or next_column >= n \
                        or visited[next_row][next_column]:
                    continue

                queue.append((next_row, next_column))
                visited[next_row][next_column] = True
                distances[next_row][next_column] = distances[row][column] + 1

        return distances
