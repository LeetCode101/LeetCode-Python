import collections
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float],
                     queries: List[List[str]]) -> List[float]:
        neighbours = collections.defaultdict(list)

        for i, (x, y) in enumerate(equations):
            value = values[i]
            neighbours[x].append((y, value))
            neighbours[y].append((x, 1 / value))

        result = []

        for x, y in queries:
            if x not in neighbours:
                result.append(-1)
            else:
                result.append(self._dfs(neighbours, x, y, 1, set()))

        return result

    def _dfs(self, neighbours, start, end, value_so_far, visited):
        if start == end:
            return value_so_far

        if start in visited:
            return -1

        visited.add(start)

        for neighbour, point in neighbours[start]:
            value = self._dfs(neighbours, neighbour, end,
                              point * value_so_far, visited)

            if value != -1:
                return value

        return -1
