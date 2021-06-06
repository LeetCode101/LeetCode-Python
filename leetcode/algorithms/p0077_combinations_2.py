from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        self._dfs(k, 1, n, [], result)

        return result

    def _dfs(self, k, start, end, combination, result):
        if k == 0:
            result.append(combination)

            return

        for i in range(start, end - k + 2):
            self._dfs(k - 1, i + 1, end,
                      combination[:] + [i], result)
