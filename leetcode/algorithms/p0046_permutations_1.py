from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        self._permute(len(nums), nums, [], permutations)

        return permutations

    def _permute(self, count, nums, permutation, permutations):
        if count == 0:
            permutations.append(permutation)

            return

        for i, n in enumerate(nums):
            self._permute(count - 1, nums[0:i] + nums[i + 1:],
                          permutation + [n], permutations)
