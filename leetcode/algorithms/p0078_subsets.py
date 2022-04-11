from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        self._search(nums, 0, [], result)

        return result

    def _search(self, nums, start, subset, result):
        result.append(subset[:])

        for i in range(start, len(nums)):
            subset.append(nums[i])

            self._search(nums, i + 1, subset, result)

            subset.pop()
