from typing import List


class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        row, column = len(mat), len(mat[0])
        left, right = 0, column

        while left <= right:
            middle = left + (right - left) // 2
            is_left = False

            for i in range(row):
                if i > 0 and mat[i - 1][middle] >= mat[i][middle]:
                    continue

                if middle > 0 and mat[i][middle - 1] >= mat[i][middle]:
                    is_left = True

                    continue

                if i + 1 < row and mat[i + 1][middle] >= mat[i][middle]:
                    continue

                if middle + 1 < column \
                        and mat[i][middle + 1] >= mat[i][middle]:
                    continue

                return [i, middle]

            if is_left:
                right = middle - 1
            else:
                left = middle + 1

        return [-1, -1]
