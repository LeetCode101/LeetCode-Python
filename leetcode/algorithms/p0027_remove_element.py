from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tail = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[tail] = nums[i]
                tail += 1

        return tail
