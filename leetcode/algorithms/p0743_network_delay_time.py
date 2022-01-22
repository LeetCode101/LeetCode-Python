import collections
import sys
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        costs = [sys.maxsize] * n
        neighbours = collections.defaultdict(list)
        queue = collections.deque([(k, 0)])

        for x, y, time in times:
            neighbours[x].append((y, time))

        while queue:
            node, time_so_far = queue.popleft()

            if time_so_far < costs[node - 1]:
                costs[node - 1] = time_so_far

                for neighbour, time in neighbours[node]:
                    queue.append((neighbour, time_so_far + time))

        max_time = max(costs)

        return max_time if max_time < sys.maxsize else -1
