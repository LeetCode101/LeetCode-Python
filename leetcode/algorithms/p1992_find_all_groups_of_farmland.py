import collections
from typing import List


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])
        result = []
        visited = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if land[i][j] == 0 or visited[i][j]:
                    continue

                visited[i][j] = True
                queue = collections.deque([(i, j)])
                top_left_x, top_left_y = i, j
                bottom_right_x, bottom_right_y = i, j

                while queue:
                    row, column = queue.popleft()
                    bottom_right_x = max(bottom_right_x, row)
                    bottom_right_y = max(bottom_right_y, column)

                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        next_row = row + dx
                        next_column = column + dy

                        if next_row < 0 or next_row >= m \
                                or next_column < 0 or next_column >= n \
                                or land[next_row][next_column] == 0 \
                                or visited[next_row][next_column]:
                            continue

                        queue.append((next_row, next_column))
                        visited[next_row][next_column] = True

                result.append([top_left_x, top_left_y,
                               bottom_right_x, bottom_right_y])

        return result
