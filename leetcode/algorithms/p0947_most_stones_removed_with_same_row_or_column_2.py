import collections
from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rows = collections.defaultdict(set)
        columns = collections.defaultdict(set)

        for x, y in stones:
            rows[x].add((x, y))
            columns[y].add((x, y))

        visited = set()
        count = 0

        for x, y in stones:
            if (x, y) in visited:
                continue

            count += self._bfs(rows, columns, x, y, visited) - 1

        return count

    def _bfs(self, rows, columns, x, y, visited):
        queue = collections.deque([(x, y)])
        count = 0
        visited.add((x, y))

        while queue:
            count += 1
            row, column = queue.popleft()

            for next_row, next_column in rows.pop(row, []):
                if (next_row, next_column) not in visited:
                    queue.append((next_row, next_column))
                    visited.add((next_row, next_column))

            for next_row, next_column in columns.pop(column, []):
                if (next_row, next_column) not in visited:
                    queue.append((next_row, next_column))
                    visited.add((next_row, next_column))

        return count
