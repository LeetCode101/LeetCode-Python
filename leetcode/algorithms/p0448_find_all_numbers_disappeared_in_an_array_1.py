from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        disappeared = []
        appeared = [0] * len(nums)

        for n in nums:
            appeared[n - 1] = 1

        for i, n in enumerate(appeared):
            if n == 0:
                disappeared.append(i + 1)

        return disappeared
