from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 1

        while i - 1 >= 0 and nums[i] <= nums[i - 1]:
            i -= 1

        if i == 0:
            nums.reverse()

            return

        j = i

        while j + 1 < n and nums[j + 1] > nums[i - 1]:
            j += 1

        nums[i - 1], nums[j] = nums[j], nums[i - 1]
        low, high = i, n - 1

        while low < high:
            nums[low], nums[high] = nums[high], nums[low]
            low += 1
            high -= 1
