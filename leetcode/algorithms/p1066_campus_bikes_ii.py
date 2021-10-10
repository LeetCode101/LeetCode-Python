import sys
from functools import lru_cache
from typing import List


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) \
            -> int:
        @lru_cache(None)
        def dfs(seen_workers, bike_index):
            if all(seen_workers):
                return 0

            min_distance = sys.maxsize
            seen_workers = list(seen_workers)

            for i in range(len(workers)):
                for j in range(bike_index, len(bikes)):
                    if seen_workers[i]:
                        continue

                    seen_workers[i] = True
                    min_distance = min(min_distance, self._get_distance(workers[i], bikes[j]) + dfs(tuple(seen_workers), j + 1))
                    seen_workers[i] = False

            return min_distance

        seen_workers = [False] * len(workers)

        return dfs(tuple(seen_workers), 0)

    def _get_distance(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
