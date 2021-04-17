from typing import List


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) \
            -> List[int]:
        counts = []
        count = 0
        roots = [-1] * (m * n)
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        for position in positions:
            root = n * position[0] + position[1]

            if roots[root] != -1:
                counts.append(count)

                continue

            count += 1
            roots[root] = root

            for direction in directions:
                x = position[0] + direction[0]
                y = position[1] + direction[1]
                neighbour = n * x + y

                if x < 0 or x >= m or y < 0 or y >= n \
                        or roots[neighbour] == -1:
                    continue

                neighbour_root = self._find_root(roots, neighbour)

                if root != neighbour_root:
                    roots[root] = neighbour_root
                    root = neighbour_root
                    count -= 1

            counts.append(count)

        return counts

    def _find_root(self, roots: List[int], id: int) -> int:
        while id != roots[id]:
            id = roots[id]

        return id
