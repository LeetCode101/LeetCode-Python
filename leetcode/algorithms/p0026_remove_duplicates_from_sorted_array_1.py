from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, length = 0, len(nums)
        size = 0

        while i < length:
            j = i + 1

            while j < length and nums[j] == nums[i]:
                j += 1

            nums[size] = nums[i]
            size += 1
            i = j

        return size
