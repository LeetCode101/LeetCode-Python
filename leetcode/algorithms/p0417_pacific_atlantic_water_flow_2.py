from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        m = len(heights)
        n = len(heights[0])
        pacific_connected = set([(i, 0) for i in range(m)]
                                + [(0, i) for i in range(n)])
        atlantic_connected = set([(i, n - 1) for i in range(m)]
                                 + [(m - 1, i) for i in range(n)])
        result = []

        pacific_connected = self._bfs(pacific_connected, heights, m, n)
        atlantic_connected = self._bfs(atlantic_connected, heights, m, n)

        for i in range(m):
            for j in range(n):
                if (i, j) in pacific_connected \
                        and (i, j) in atlantic_connected:
                    result.append([i, j])

        return result

    def _bfs(self, connected, heights, m, n):
        queue = deque(connected)

        while queue:
            row, column = queue.popleft()

            for direction in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_row, new_column = row + direction[0], column + direction[1]

                if new_row < 0 or new_row >= m \
                        or new_column < 0 or new_column >= n \
                        or (new_row, new_column) in connected \
                        or heights[row][column] > heights[new_row][new_column]:
                    continue

                queue.append((new_row, new_column))
                connected.add((new_row, new_column))

        return connected
