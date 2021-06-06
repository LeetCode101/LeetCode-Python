import functools
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        return self._dfs(tuple(nums), target)

    @functools.lru_cache(None)
    def _dfs(self, candidates, target):
        if target == 0:
            return 1

        count = 0

        for n in candidates:
            if n > target:
                continue

            count += self._dfs(candidates, target - n)

        return count
