from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = set()
        n = len(nums)

        for i in range(n):
            while nums[i] != i + 1:
                j = nums[i] - 1

                if nums[i] != nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                else:
                    duplicates.add(nums[i])

                    break

        return list(duplicates)
