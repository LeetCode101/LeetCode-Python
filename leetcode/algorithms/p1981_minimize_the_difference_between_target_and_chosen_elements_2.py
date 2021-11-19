import functools
import sys
from typing import List


class Solution:
    def __init__(self):
        self.min_diff = sys.maxsize

    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        @functools.lru_cache(None)
        def _dfs(row, target):
            if row < 0:
                self.min_diff = min(self.min_diff, abs(target))

                return abs(target)

            if target < 0 and abs(target) > self.min_diff:
                return sys.maxsize

            current_diff = sys.maxsize

            for column in range(len(mat[0])):
                if column > 0 and mat[row][column] == mat[row][column - 1]:
                    continue

                current_diff = min(current_diff,
                                   _dfs(row - 1, target - mat[row][column]))

                if current_diff == 0:
                    break

            return current_diff

        for row in mat:
            row.sort()

        return _dfs(len(mat) - 1, target)
