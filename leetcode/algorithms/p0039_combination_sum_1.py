from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) \
            -> List[List[int]]:
        result = []

        self._dfs(candidates, 0, target, [], result)

        return result

    def _dfs(self, candidates, start, target, combination, result):
        if target < 0:
            return
        elif target == 0:
            result.append(combination)

            return

        for i in range(start, len(candidates)):
            n = candidates[i]

            self._dfs(candidates, i, target - n, combination[:] + [n], result)
