from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []

        for i in range(n):
            if nums[i] == i + 1:
                continue

            while nums[i] != i + 1:
                k = nums[i]
                nums[i], nums[k - 1] = nums[k - 1], nums[i]

                if nums[i] == nums[k - 1]:
                    break

        for i in range(n):
            if nums[i] != i + 1:
                result.append(i + 1)

        return result
