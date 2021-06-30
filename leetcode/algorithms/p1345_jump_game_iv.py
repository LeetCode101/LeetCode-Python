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

        while queue:
            steps, i = queue.popleft()

            if i < 0 or i >= len(arr) or i in visited:
                continue

            if i == n - 1:
                return steps

            visited.add(i)
            queue.append((steps + 1, i + 1))
            queue.append((steps + 1, i - 1))

            if arr[i] in positions:
                for neighbour in positions[arr[i]]:
                    queue.append((steps + 1, neighbour))

                positions.pop(arr[i])
