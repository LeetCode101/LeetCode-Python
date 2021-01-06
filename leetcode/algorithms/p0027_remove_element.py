from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        tail = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[tail] = nums[i]
                count += 1
                tail += 1

        return count
