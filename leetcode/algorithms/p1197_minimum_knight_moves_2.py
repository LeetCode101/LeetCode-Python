import collections


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        visited = set()
        queue = collections.deque([(0, 0, 0)])
        x, y = abs(x), abs(y)

        while queue:
            row, column, distance = queue.popleft()

            if row == x and column == y:
                return distance

            for dx, dy in [(1, 2), (2, 1), (1, -2), (2, -1),
                           (-1, -2), (-2, -1), (-1, 2), (-2, 1)]:
                next_row = row + dx
                next_column = column + dy

                if (next_row, next_column) in visited:
                    continue

                if next_row < -2 or next_column < -2:
                    continue

                visited.add((next_row, next_column))
                queue.append((next_row, next_column, distance + 1))

        return -1
