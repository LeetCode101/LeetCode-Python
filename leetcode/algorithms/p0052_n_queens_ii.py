from typing import Set


class Solution:
    def totalNQueens(self, n: int) -> int:
        return self._dfs(0, n, set(), set(), set())

    def _dfs(self, row: int, n, columns: Set[int], left_diagonals: Set[int],
             right_diagonals: Set[int]) -> int:
        if row == n:
            return 1

        count = 0

        for column in range(n):
            if column in columns or row + column in left_diagonals \
                    or row - column in right_diagonals:
                continue

            columns.add(column)
            left_diagonals.add(row + column)
            right_diagonals.add(row - column)

            count += self._dfs(row + 1, n, columns, left_diagonals,
                               right_diagonals)

            columns.remove(column)
            left_diagonals.remove(row + column)
            right_diagonals.remove(row - column)

        return count
