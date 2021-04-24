from typing import List


# Time Limit Exceeded!
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self._dfs(nums, 0, 0, target)

    def _dfs(self, nums, i, sum_so_far, target):
        if i == len(nums):
            return 1 if sum_so_far == target else 0

        return self._dfs(nums, i + 1, sum_so_far + nums[i], target) + \
            self._dfs(nums, i + 1, sum_so_far - nums[i], target)
