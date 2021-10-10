import collections
import sys
from typing import List


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) \
            -> int:
        memo = collections.defaultdict(int)

        return self._dfs(workers, bikes, 0, 0, memo)

    def _dfs(self, workers, bikes, worker_index, seen_bikes, memo):
        if worker_index == len(workers):
            return 0

        if seen_bikes in memo:
            return memo[seen_bikes]

        min_distance_sum = sys.maxsize

        for i in range(len(bikes)):
            if (seen_bikes >> i) & 1 == 1:
                continue

            distance = self._get_distance(workers[worker_index], bikes[i])
            current_distance_sum = distance + self._dfs(
                workers, bikes, worker_index + 1, seen_bikes | (1 << i), memo)
            min_distance_sum = min(min_distance_sum, current_distance_sum)

        memo[seen_bikes] = min_distance_sum

        return min_distance_sum

    def _get_distance(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
