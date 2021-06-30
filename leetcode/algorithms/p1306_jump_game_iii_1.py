from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        return self._dfs(arr, start, set())

    def _dfs(self, arr, start, visited):
        if start < 0 or start >= len(arr) or start in visited:
            return False

        if arr[start] == 0:
            return True

        visited.add(start)

        return self._dfs(arr, start + arr[start], visited) \
            or self._dfs(arr, start - arr[start], visited)
