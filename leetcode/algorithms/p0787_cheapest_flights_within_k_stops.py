import collections
import sys
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]],
                          src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        prices = collections.defaultdict(lambda: sys.maxsize)

        for x, y, price in flights:
            graph[x].append((y, price))

        queue = collections.deque([(src, -1, 0)])

        while queue:
            node, jumps, cost = queue.popleft()

            if node == dst or jumps == k:
                continue

            for neighbour, price in graph[node]:
                if cost + price > prices[neighbour]:
                    continue
                else:
                    prices[neighbour] = cost + price
                    queue.append((neighbour, jumps + 1, cost + price))

        return prices[dst] if prices[dst] != sys.maxsize else -1
