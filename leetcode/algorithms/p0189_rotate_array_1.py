from typing import List


# Time Limit Exceeded!
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        step = k % len(nums)
        length = len(nums)

        for i in range(step):
            temp = nums[length - step + i]

            for j in range(length - step + i, i, -1):
                nums[j], nums[j - 1] = nums[j - 1], nums[j]

            nums[i] = temp
