from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        sums = {}
        sum_so_far = 0
        max_length = 0

        for i, n in enumerate(nums):
            sum_so_far += n

            if sum_so_far == k:
                max_length = i + 1
            elif (sum_so_far - k) in sums:
                max_length = max(max_length, i - sums[sum_so_far - k])

            if sum_so_far not in sums:
                sums[sum_so_far] = i

        return max_length
