from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) \
            -> int:
        neighbours = [[] for _ in range(n)]

        for x, y in edges:
            neighbours[x].append(y)
            neighbours[y].append(x)

        return self._dfs(0, neighbours, set(), hasApple)

    def _dfs(self, node, neighbours, visited, has_apple):
        if node in visited:
            return 0

        visited.add(node)
        seconds = 0

        for neighbour in neighbours[node]:
            seconds += self._dfs(neighbour, neighbours, visited, has_apple)

        if (seconds > 0 or has_apple[node]) and node != 0:
            return seconds + 2
        else:
            return seconds
