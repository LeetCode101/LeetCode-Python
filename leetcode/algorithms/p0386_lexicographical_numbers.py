from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []

        self._dfs(0, n, result)

        return result

    def _dfs(self, current, n, result):
        for i in range(10):
            x = current * 10 + i

            if x > n:
                return

            if x != 0:
                result.append(x)

                self._dfs(x, n, result)
