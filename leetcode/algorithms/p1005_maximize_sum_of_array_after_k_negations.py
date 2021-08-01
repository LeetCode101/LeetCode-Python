from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        i = 0

        while k > 0 and sorted_nums[i] <= 0:
            sorted_nums[i] = -sorted_nums[i]
            k -= 1
            i += 1

        if k & 1 == 1:
            target = i

            if i > 0 and sorted_nums[i - 1] < sorted_nums[i]:
                target = i - 1

            sorted_nums[target] = -sorted_nums[target]

        return sum(sorted_nums)
