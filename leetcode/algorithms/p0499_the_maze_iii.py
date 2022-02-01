import heapq
from typing import List


class Solution:
    def findShortestWay(self, maze: List[List[int]],
                        ball: List[int], hole: List[int]) -> str:
        m, n = len(maze), len(maze[0])
        heap = [(0, '', ball[0], ball[1])]
        heapq.heapify(heap)
        distances = [[(-1, '') for _ in range(n)] for _ in range(m)]
        distances[ball[0]][ball[1]] = (0, '')

        while heap:
            distance, path, row, column = heapq.heappop(heap)

            if row == hole[0] and column == hole[1]:
                return path

            for dx, dy, direction in [(0, -1, 'l'), (-1, 0, 'u'),
                                      (0, 1, 'r'), (1, 0, 'd')]:
                next_row = row
                next_column = column
                jumps = 0
                current_path = path + direction

                while 0 <= next_row + dx < m and 0 <= next_column + dy < n \
                        and maze[next_row + dx][next_column + dy] == 0:
                    next_row += dx
                    next_column += dy
                    jumps += 1

                    if next_row == hole[0] and next_column == hole[1]:
                        break

                current_distance = distance + jumps

                if distances[next_row][next_column][0] == -1 \
                        or distances[next_row][next_column] \
                        > (current_distance, current_path):
                    distances[next_row][next_column] = \
                        (current_distance, current_path)
                    heapq.heappush(heap, (current_distance, current_path,
                                          next_row, next_column))

        return 'impossible'
