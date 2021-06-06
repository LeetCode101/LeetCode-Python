from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) \
            -> List[List[int]]:
        result = []

        self._dfs(sorted(candidates), 0, target, [], result)

        return result

    def _dfs(self, candidates, start, target, combination, result):
        if target == 0:
            result.append(combination)

            return

        for i in range(start, len(candidates)):
            n = candidates[i]

            if n > target:
                break

            self._dfs(candidates, i, target - n, combination[:] + [n], result)
