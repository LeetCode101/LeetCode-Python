from typing import List, Set


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        visited = set()

        return self.dfs(arr, 0, visited)

    def dfs(self, arr: List[str], start: int, visited: Set[str]) -> int:
        max_length = len(visited)

        if start == len(arr):
            return max_length

        for i in range(start, len(arr)):
            if not self.is_unique(arr[i], visited):
                continue

            visited.update(list(arr[i]))

            max_length = max(self.dfs(arr, i + 1, visited), max_length)

            visited.difference_update(list(arr[i]))

        return max_length

    def is_unique(self, word: str, visited: Set[str]) -> bool:
        for c in word:
            if c in visited:
                return False

        return len(word) == len(set(list(word)))
