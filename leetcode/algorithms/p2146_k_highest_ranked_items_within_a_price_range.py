import collections
import heapq
from typing import List


class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int],
                            start: List[int], k: int) -> List[List[int]]:
        heap = []
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        queue = collections.deque([(start[0], start[1], 0)])

        while queue:
            row, column, distance = queue.popleft()

            if visited[row][column]:
                continue

            visited[row][column] = True

            if pricing[0] <= grid[row][column] <= pricing[1]:
                heapq.heappush(heap, (-distance, -grid[row][column],
                                      -row, -column))

            if len(heap) > k:
                heapq.heappop(heap)

            for dx, dy in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                next_row = row + dx
                next_column = column + dy

                if 0 <= next_row < m and 0 <= next_column < n \
                        and not visited[next_row][next_column] \
                        and grid[next_row][next_column] != 0:
                    queue.append((next_row, next_column, distance + 1))

        return [[-x[2], -x[3]] for x in sorted(heap, reverse=True)]
