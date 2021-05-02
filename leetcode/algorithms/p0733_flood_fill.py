from typing import List


class Solution:
    def floodFill(self, image: List[List[int]],
                  sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image:
            return []

        m, n = len(image), len(image[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        self._dfs(image, sr, sc, image[sr][sc], newColor, visited)

        return image

    def _dfs(self, image, row, column, current_color, new_color, visited):
        m, n = len(image), len(image[0])

        if row < 0 or row >= m or column < 0 or column >= n \
                or image[row][column] != current_color \
                or visited[row][column]:
            return

        visited[row][column] = True
        image[row][column] = new_color

        for direction in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            self._dfs(image, row + direction[0],
                      column + direction[1], current_color, new_color, visited)
