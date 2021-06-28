from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = 0

        for i, step in enumerate(nums):
            if i > end:
                return False

            end = max(end, i + step)

        return True
