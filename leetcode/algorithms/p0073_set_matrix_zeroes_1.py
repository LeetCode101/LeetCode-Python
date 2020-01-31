from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return

        m, n = len(matrix), len(matrix[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0 and not visited[i][j]:
                    for k in range(m):
                        if k != i and matrix[k][j] != 0:
                            matrix[k][j] = 0
                            visited[k][j] = True

                    for k in range(n):
                        if k != j and matrix[i][k] != 0:
                            matrix[i][k] = 0
                            visited[i][k] = True

                    visited[i][j] = True
