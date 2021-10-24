import collections
from typing import List


# Time Limit Exceeded!
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        neighbours = collections.defaultdict(list)

        for edge in edges:
            neighbours[edge[0]].append(edge[1])
            neighbours[edge[1]].append(edge[0])

        min_height = n
        result = []

        for i in range(n):
            visited = set()
            height = 0
            queue = collections.deque([i])

            while queue:
                height += 1
                size = len(queue)

                if height > min_height:
                    break

                for _ in range(size):
                    node = queue.popleft()
                    visited.add(node)

                    for neighbour in neighbours[node]:
                        if neighbour not in visited:
                            queue.append(neighbour)

            if height == min_height:
                result.append(i)
            elif height < min_height:
                result = [i]
                min_height = height

        return result
