from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        i = 0

        while i < n:
            j = i + 2

            if j < n and nums[j] - nums[j - 1] == nums[j - 1] - nums[j - 2]:
                j += 1

                while j < n and nums[j] - nums[j - 1] == nums[i + 1] - nums[i]:
                    j += 1

                size = j - i
                count += (size - 1) * (size - 2) // 2
                i = j - 1
            else:
                i += 1

        return count
