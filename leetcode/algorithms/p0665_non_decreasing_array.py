from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modified = False
        n = len(nums)

        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                if modified:
                    return False

                if (i - 2 >= 0 and nums[i - 2] > nums[i]) \
                        and (i + 1 < n and nums[i - 1] > nums[i + 1]):
                    return False

                modified = True

        return True
