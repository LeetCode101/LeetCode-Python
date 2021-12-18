import collections
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        neighbours = collections.defaultdict(list)

        for a, b in edges:
            neighbours[a].append(b)
            neighbours[b].append(a)

        count = 0
        visited = set()

        for i in range(n):
            if i not in visited:
                self._dfs(neighbours, visited, i)
                count += 1

        return count

    def _dfs(self, neighbours, visited, i):
        if i not in neighbours:
            return

        stack = [i]

        while stack:
            for neighbour in neighbours.pop(stack.pop(), []):
                if neighbour in visited:
                    continue

                visited.add(neighbour)
                stack.append(neighbour)
