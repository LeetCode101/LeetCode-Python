from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        candidates = set([i + 1 for i in range(n)])

        self._dfs(k, 0, candidates, [], result)

        return result

    def _dfs(self, k, prev_candidate, candidates, combination, result):
        if k == 0:
            result.append(combination)

            return

        for n in candidates:
            if n <= prev_candidate:
                continue

            new_candidates = set(candidates)
            new_candidates.remove(n)

            self._dfs(k - 1, n, new_candidates,
                      combination[:] + [n], result)
