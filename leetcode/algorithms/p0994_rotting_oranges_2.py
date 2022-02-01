from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        stack = []
        m, n = len(grid), len(grid[0])
        fresh_count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    stack.append((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1

        minutes = 0
        visited = [[False] * n for _ in range(m)]

        while stack:
            size = len(stack)
            new_stack = []
            affected = False

            for _ in range(size):
                row, column = stack.pop()
                visited[row][column] = True

                for dx, dy in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                    next_row = row + dx
                    next_column = column + dy

                    if 0 <= next_row < m and 0 <= next_column < n \
                            and not visited[next_row][next_column] \
                            and grid[next_row][next_column] == 1:
                        affected = True
                        fresh_count -= 1
                        visited[next_row][next_column] = True
                        new_stack.append((next_row, next_column))

            if affected:
                minutes += 1

            stack = new_stack

        return minutes if fresh_count == 0 else -1
