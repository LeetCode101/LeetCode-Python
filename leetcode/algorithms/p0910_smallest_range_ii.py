from typing import List


class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        min_score = sorted_nums[-1] - sorted_nums[0]

        for i in range(len(sorted_nums) - 1):
            big = max(sorted_nums[i] + k, sorted_nums[-1] - k)
            small = min(sorted_nums[i + 1] - k, sorted_nums[0] + k)
            min_score = min(min_score, big - small)

        return min_score
