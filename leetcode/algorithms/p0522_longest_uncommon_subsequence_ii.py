from typing import List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        n = len(strs)
        strs = sorted(strs, key=lambda x: len(x), reverse=True)

        for i in range(n):
            miss_match_count = n - 1

            for j in range(n):
                if i == j:
                    continue

                if not self._is_sub_sequence(strs[i], strs[j]):
                    miss_match_count -= 1

            if miss_match_count == 0:
                return len(strs[i])

        return -1

    def _is_sub_sequence(self, a, b):
        i = 0
        n = len(a)

        for j, c in enumerate(b):
            if i < n and c == a[i]:
                i += 1

        return i == n
