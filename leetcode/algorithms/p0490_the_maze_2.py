from typing import List


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int],
                destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        visited = [[False] * n for _ in range(m)]
        stack = [(start[0], start[1])]

        while stack:
            row, column = stack.pop()

            if row == destination[0] and column == destination[1]:
                return True

            if visited[row][column]:
                continue

            visited[row][column] = True

            for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                next_row = row
                next_column = column

                while 0 <= next_row + dx < m and 0 <= next_column + dy < n \
                        and maze[next_row + dx][next_column + dy] == 0:
                    next_row += dx
                    next_column += dy

                stack.append((next_row, next_column))

        return False
