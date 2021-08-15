import sys


class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        return self._dfs(s, 0, k, {})

    def _cost(self, s, i, j):
        cost = 0

        while i < j:
            if s[i] != s[j]:
                cost += 1

            i += 1
            j -= 1

        return cost

    def _dfs(self, s, i, k, cache):
        if (i, k) in cache:
            return cache[(i, k)]

        if len(s) - i == k:
            return 0

        if k == 1:
            return self._cost(s, i, len(s) - 1)

        cut = sys.maxsize

        for j in range(i + 1, len(s) - k + 2):
            current_cut = self._dfs(s, j, k - 1, cache) \
                          + self._cost(s, i, j - 1)
            cut = min(cut, current_cut)

        cache[(i, k)] = cut

        return cut
