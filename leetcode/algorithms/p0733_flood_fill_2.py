from collections import deque
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]],
                  sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image:
            return []

        m, n = len(image), len(image[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        current_color = image[sr][sc]
        visited[sr][sc] = True
        queue = deque([(sr, sc)])

        while queue:
            cell = queue.popleft()
            row, column = cell[0], cell[1]
            image[row][column] = newColor

            for direction in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                next_row = row + direction[0]
                next_column = column + direction[1]

                if next_row < 0 or next_row >= m \
                        or next_column < 0 \
                        or next_column >= n \
                        or image[next_row][next_column] != current_color \
                        or visited[next_row][next_column]:
                    continue

                queue.append((next_row, next_column))
                visited[next_row][next_column] = True

        return image
