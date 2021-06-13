from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        self._permute(len(nums), set(nums), [], permutations)

        return permutations

    def _permute(self, count, nums, permutation, permutations):
        if count == 0:
            permutations.append(permutation)

            return

        for n in nums:
            new_nums = set(nums)
            new_nums.remove(n)

            self._permute(count - 1, new_nums, permutation + [n], permutations)
