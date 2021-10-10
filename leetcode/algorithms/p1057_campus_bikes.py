from typing import List


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) \
            -> List[int]:
        pairs = []

        for i, (x, y) in enumerate(workers):
            for j, (m, n) in enumerate(bikes):
                pairs.append((abs(x - m) + abs(y - n), i, j))

        result = [-1] * len(workers)
        seen = [False] * len(bikes)

        for _, i, j in sorted(pairs):
            if result[i] == -1 and not seen[j]:
                result[i] = j
                seen[j] = True

        return result
