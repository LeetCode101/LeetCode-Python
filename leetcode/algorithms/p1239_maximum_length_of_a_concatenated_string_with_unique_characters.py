from typing import List, Set


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        visited = set()

        return self._dfs(arr, 0, visited)

    def _dfs(self, arr: List[str], start: int, visited: Set[str]) -> int:
        max_length = len(visited)

        if start == len(arr):
            return max_length

        for i in range(start, len(arr)):
            if not self._is_unique(arr[i], visited):
                continue

            visited.update(list(arr[i]))

            max_length = max(self._dfs(arr, i + 1, visited), max_length)

            visited.difference_update(list(arr[i]))

        return max_length

    def _is_unique(self, word: str, visited: Set[str]) -> bool:
        for c in word:
            if c in visited:
                return False

        return len(word) == len(set(list(word)))
