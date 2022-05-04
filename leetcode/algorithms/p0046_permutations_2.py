from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        self._dfs(nums, 0, [], result, set())

        return result

    def _dfs(self, nums, start, current, result, visited):
        if start == len(nums):
            result.append(current[:])

            return

        for n in nums:
            if n in visited:
                continue

            current.append(n)
            visited.add(n)

            self._dfs(nums, start + 1, current, result, visited)

            current.pop()
            visited.remove(n)
