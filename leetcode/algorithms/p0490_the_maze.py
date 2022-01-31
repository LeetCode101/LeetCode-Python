from typing import List


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int],
                destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        visited = [[False] * n for _ in range(m)]

        return self._dfs(maze, start, destination, visited)

    def _dfs(self, maze, start, end, visited):
        row, column = start
        m, n = len(maze), len(maze[0])

        if row == end[0] and column == end[1]:
            return True

        if visited[row][column]:
            return False

        visited[row][column] = True

        for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            next_row = row
            next_column = column

            while 0 <= next_row + dx < m and 0 <= next_column + dy < n \
                    and maze[next_row + dx][next_column + dy] == 0:
                next_row += dx
                next_column += dy

            if self._dfs(maze, [next_row, next_column], end, visited):
                return True

        return False
