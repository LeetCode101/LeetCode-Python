from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        tail = 0
        duplicates = 1

        for i in range(1, len(nums)):
            if nums[tail] != nums[i]:
                duplicates = 1
            else:
                duplicates += 1

            if duplicates <= 2:
                tail += 1
                nums[tail] = nums[i]

        return tail + 1
