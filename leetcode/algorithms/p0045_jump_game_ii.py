from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0
        max_end = 0

        for i in range(len(nums) - 1):
            step = nums[i]
            max_end = max(max_end, i + step)

            if i == current_end:
                jumps += 1
                current_end = max_end

        return jumps
