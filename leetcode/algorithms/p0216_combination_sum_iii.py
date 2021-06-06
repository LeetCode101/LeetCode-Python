from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        self._dfs(1, 9, k, n, [], result)

        return result

    def _dfs(self, start, end, k, target, combination, result):
        if k == 0 and target == 0:
            result.append(combination)

            return

        for n in range(start, end - k + 2):
            if n > target:
                break

            self._dfs(n + 1, end, k - 1, target - n,
                      combination[:] + [n], result)
