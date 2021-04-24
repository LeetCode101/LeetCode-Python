from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self._dfs(nums, 0, 0, target)

    def _dfs(self, nums, i, value, target):
        if i == len(nums):
            return 1 if value == target else 0

        return self._dfs(nums, i + 1, value + nums[i], target) + \
            self._dfs(nums, i + 1, value - nums[i], target)
