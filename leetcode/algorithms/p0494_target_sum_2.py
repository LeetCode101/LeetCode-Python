from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        return self._dfs(nums, 0, 0, target, memo)

    def _dfs(self, nums, i, value, target, memo):
        if (i, value) in memo:
            return memo[(i, value)]

        if i == len(nums):
            return 1 if value == target else 0

        count = self._dfs(nums, i + 1, value + nums[i], target, memo) + \
            self._dfs(nums, i + 1, value - nums[i], target, memo)
        memo[(i, value)] = count

        return count
