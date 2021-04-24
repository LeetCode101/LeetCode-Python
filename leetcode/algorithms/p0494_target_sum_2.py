from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        return self._dfs(nums, 0, 0, target, memo)

    def _dfs(self, nums, i, sum_so_far, target, memo):
        if (i, sum_so_far) in memo:
            return memo[(i, sum_so_far)]

        if i == len(nums):
            return 1 if sum_so_far == target else 0

        count = self._dfs(nums, i + 1, sum_so_far + nums[i], target, memo) + \
            self._dfs(nums, i + 1, sum_so_far - nums[i], target, memo)
        memo[(i, sum_so_far)] = count

        return count
