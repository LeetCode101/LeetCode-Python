from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        size, length = 0, len(nums)

        for i in range(1, length):
            if nums[i] == nums[size]:
                continue
            else:
                size += 1
                nums[size] = nums[i]

        return size + 1
