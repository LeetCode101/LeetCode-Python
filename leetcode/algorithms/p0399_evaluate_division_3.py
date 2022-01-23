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
                result.append(self._bfs(neighbours, x, y))

        return result

    def _bfs(self, neighbours, start, end):
        queue = collections.deque([(start, 1)])
        visited = set()

        while queue:
            current, value_so_far = queue.popleft()

            if current == end:
                return value_so_far

            visited.add(current)

            for neighbour, point in neighbours[current]:
                if neighbour not in visited:
                    queue.append((neighbour, point * value_so_far))

        return -1
