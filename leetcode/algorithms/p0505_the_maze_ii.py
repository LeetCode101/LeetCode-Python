import heapq
from typing import List


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int],
                         destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        heap = [(0, start[0], start[1])]
        heapq.heapify(heap)
        distances = [[-1] * n for _ in range(m)]

        while heap:
            distance, row, column = heapq.heappop(heap)

            if row == destination[0] and column == destination[1]:
                return distance

            for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                next_row = row
                next_column = column
                jumps = 0

                while 0 <= next_row + dx < m and 0 <= next_column + dy < n \
                        and maze[next_row + dx][next_column + dy] == 0:
                    next_row += dx
                    next_column += dy
                    jumps += 1

                current_distance = distance + jumps

                if distances[next_row][next_column] == -1 \
                        or distances[next_row][next_column] > current_distance:
                    distances[next_row][next_column] = current_distance
                    heapq.heappush(heap,
                                   (current_distance, next_row, next_column))

        return -1
