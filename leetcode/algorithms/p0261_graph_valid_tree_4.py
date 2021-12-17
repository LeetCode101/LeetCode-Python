from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        neighbours = {i: [] for i in range(n)}

        for a, b in edges:
            neighbours[a].append(b)
            neighbours[b].append(a)

        stack = [0]

        while stack:
            for neighbour in neighbours.pop(stack.pop(), []):
                stack.append(neighbour)

        return len(edges) == n - 1 and not neighbours
