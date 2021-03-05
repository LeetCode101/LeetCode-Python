from typing import List, Set


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []

        self._dfs(0, n, set(), set(), set(), [], result)

        return [['.' * i + 'Q' + '.' * (n - i - 1) for i in solution]
                for solution in result]

    def _dfs(self, row: int, n, columns: Set[int], left_diagonals: Set[int],
             right_diagonals: Set[int], solution: List[int],
             result: List[List[int]]) -> None:
        if row == n:
            result.append(solution)

            return

        for column in range(n):
            if column in columns or row + column in left_diagonals \
                    or row - column in right_diagonals:
                continue

            columns.add(column)
            left_diagonals.add(row + column)
            right_diagonals.add(row - column)

            self._dfs(row + 1, n, columns, left_diagonals,
                      right_diagonals, solution + [column], result)

            columns.remove(column)
            left_diagonals.remove(row + column)
            right_diagonals.remove(row - column)
