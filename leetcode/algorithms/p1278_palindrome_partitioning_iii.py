import sys


class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        return self._dfs(s, 0, k, {})

    def _cost(self, s, start, end):
        cost = 0

        while start < end:
            if s[start] != s[end]:
                cost += 1

            start += 1
            end -= 1

        return cost

    def _dfs(self, s, start, k, cache):
        if (start, k) in cache:
            return cache[(start, k)]

        if len(s) - start == k:
            return 0

        if k == 1:
            return self._cost(s, start, len(s) - 1)

        cut = sys.maxsize

        for end in range(start, len(s) - k + 1):
            current_cut = self._dfs(s, end + 1, k - 1, cache) \
                          + self._cost(s, start, end)
            cut = min(cut, current_cut)

        cache[(start, k)] = cut

        return cut
