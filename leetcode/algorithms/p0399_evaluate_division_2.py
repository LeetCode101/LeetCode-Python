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
                result.append(self._dfs(neighbours, x, y))

        return result

    def _dfs(self, neighbours, start, end):
        stack = [(start, 1)]
        visited = set()

        while stack:
            current, value_so_far = stack.pop()

            if current == end:
                return value_so_far

            visited.add(current)

            for neighbour, point in neighbours[current]:
                if neighbour not in visited:
                    stack.append((neighbour, point * value_so_far))

        return -1
