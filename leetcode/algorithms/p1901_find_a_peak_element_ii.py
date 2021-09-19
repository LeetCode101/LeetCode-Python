from typing import List


class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        row, column = len(mat), len(mat[0])
        i, j = 0, column - 1
        visited = set()

        while 0 <= i < row and 0 <= j < column:
            if (i, j) in visited:
                break

            visited.add((i, j))

            up = -1 if i - 1 < 0 else mat[i - 1][j]
            down = -1 if i + 1 >= row else mat[i + 1][j]
            left = -1 if j - 1 < 0 else mat[i][j - 1]
            right = -1 if j + 1 >= column else mat[i][j + 1]
            current = mat[i][j]

            if current > up and current > down \
                    and current > left and current > right:
                return [i, j]

            max_value = max(up, down, left, right)

            if up == max_value:
                i -= 1
            elif down == max_value:
                i += 1
            elif left == max_value:
                j -= 1
            elif right == max_value:
                j += 1

        return [-1, -1]
