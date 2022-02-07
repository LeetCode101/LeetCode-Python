import collections
from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int],
                     informTime: List[int]) -> int:
        graph = collections.defaultdict(list)

        for i, x in enumerate(manager):
            if i != headID:
                graph[x].append(i)

        cost = 0
        stack = [(headID, 0)]

        while stack:
            node, current_cost = stack.pop()

            for child in graph[node]:
                stack.append((child, current_cost + informTime[node]))

            if not graph[node]:
                cost = max(cost, current_cost)

        return cost
