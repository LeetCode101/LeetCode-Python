from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []

        self._search(sorted(nums), 0, [], result)

        return result

    def _search(self, nums, start, subset, result):
        result.append(subset[:])

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue

            subset.append(nums[i])

            self._search(nums, i + 1, subset, result)

            subset.pop()
