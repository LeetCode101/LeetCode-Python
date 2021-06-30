import collections
from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if not arr:
            return 0

        n = len(arr)
        positions = collections.defaultdict(list)

        for i, step in enumerate(arr):
            positions[step].append(i)

        queue = collections.deque([(0, 0)])
        visited = set()
        visited_groups = set()

        while queue:
            steps, i = queue.popleft()

            if i == n - 1:
                return steps

            for neighbour in [i - 1, i + 1]:
                if 0 <= neighbour < n and neighbour not in visited:
                    visited.add(n)
                    queue.append((steps + 1, neighbour))

            if arr[i] not in visited_groups:
                for neighbour in positions[arr[i]]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.append((steps + 1, neighbour))

                visited_groups.add(arr[i])
