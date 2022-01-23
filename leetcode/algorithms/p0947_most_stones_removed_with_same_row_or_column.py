import collections
from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        max_row = 0
        max_column = 0
        rows = collections.defaultdict(set)
        columns = collections.defaultdict(set)

        for x, y in stones:
            max_row = max(max_row, x + 1)
            max_column = max(max_column, y + 1)
            rows[x].add((x, y))
            columns[y].add((x, y))

        visited = set()
        count = 0

        for x, y in stones:
            if (x, y) in visited:
                continue

            count += self._dfs(rows, columns, x, y, visited) - 1

        return count

    def _dfs(self, rows, columns, x, y, visited):
        stack = [(x, y)]
        count = 0

        while stack:
            row, column = stack.pop()

            for next_row, next_column in rows.pop(row, []):
                if (next_row, next_column) not in visited:
                    stack.append((next_row, next_column))
                    visited.add((next_row, next_column))

            for next_row, next_column in columns.pop(column, []):
                if (next_row, next_column) not in visited:
                    stack.append((next_row, next_column))
                    visited.add((next_row, next_column))

            if stack:
                count += 1

        return count
