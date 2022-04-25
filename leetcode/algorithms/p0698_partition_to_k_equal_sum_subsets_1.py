from typing import List


# Time Limit Exceeded!
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        n = len(nums)

        if n < k or total % k != 0:
            return False

        visited = [False] * n

        return self._dfs(nums, visited, 0, k, 0, total // k)

    def _dfs(self, nums, visited, start, k, current_sum, target):
        if k == 1:
            return True

        if current_sum > target:
            return False

        if current_sum == target:
            return self._dfs(nums, visited, 0, k - 1, 0, target)

        for i in range(start, len(nums)):
            if visited[i]:
                continue

            visited[i] = True

            if self._dfs(nums, visited, i + 1, k,
                         current_sum + nums[i], target):
                return True

            visited[i] = False

        return False
