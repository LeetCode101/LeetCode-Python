from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) \
            -> int:
        neighbours = [[] for _ in range(n)]

        for x, y in edges:
            neighbours[x].append(y)
            neighbours[y].append(x)

        return max(self._dfs(0, neighbours, set(), hasApple) - 2, 0)

    def _dfs(self, node, neighbours, visited, has_apple):
        if node in visited:
            return 0

        visited.add(node)
        seconds = 0

        for neighbour in neighbours[node]:
            seconds += self._dfs(neighbour, neighbours, visited, has_apple)

        if seconds > 0:
            return seconds + 2

        return 2 if has_apple[node] else 0
