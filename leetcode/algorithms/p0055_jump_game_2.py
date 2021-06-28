from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = 0
        n = len(nums)

        for i in range(n - 1):
            step = nums[i]

            if i > end:
                return False

            end = max(end, i + step)

        return end >= n - 1
