from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        tail, length = 0, len(nums)

        for i in range(1, length):
            if nums[i] != nums[tail]:
                tail += 1
                nums[tail] = nums[i]

        return tail + 1
