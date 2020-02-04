from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red, blue = 0, len(nums) - 1
        i = 0

        while i <= blue:
            if nums[i] == 0:
                nums[i], nums[red] = nums[red], nums[i]
                red += 1
            elif nums[i] == 2:
                nums[i], nums[blue] = nums[blue], nums[i]
                blue -= 1
                i -= 1

            i += 1
