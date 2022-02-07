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
        queue = collections.deque([(headID, 0)])

        while queue:
            node, current_cost = queue.popleft()

            for child in graph[node]:
                queue.append((child, current_cost + informTime[node]))

            if not graph[node]:
                cost = max(cost, current_cost)

        return cost
