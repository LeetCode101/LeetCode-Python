from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        matrix = [[''] * m for _ in range(n)]

        for i in range(m):
            for j in range(n):
                matrix[j][m - i - 1] = box[i][j]

        for i in range(m):
            tail = n - 1

            for j in range(n - 1, -1, -1):
                cell = matrix[j][i]

                if cell == '*':
                    tail = j - 1
                elif cell == '#':
                    if tail != j:
                        matrix[tail][i], matrix[j][i] = matrix[j][i], '.'

                    tail -= 1

        return matrix
