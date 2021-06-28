from typing import List


# Time Limit Exceeded!
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return self._dfs(tuple(nums), 0)

    def _dfs(self, nums, start):
        if start == len(nums):
            return True

        for step in range(nums[start]):
            if self._dfs(nums, start + step + 1):
                return True

        return nums[start] == 0 and start == len(nums) - 1
