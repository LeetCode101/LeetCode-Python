from typing import List


class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int,
                           secondLen: int) -> int:
        prefix_sum = [0] * (len(nums) + 1)

        for i, n in enumerate(nums):
            prefix_sum[i + 1] = prefix_sum[i] + n

        return max(self._max_sum(prefix_sum, firstLen, secondLen),
                   self._max_sum(prefix_sum, secondLen, firstLen))

    def _max_sum(self, prefix_sum, first_length, second_length):
        max_left_sum = 0
        max_sum = 0

        for i in range(first_length + second_length, len(prefix_sum)):
            current_left_sum = prefix_sum[i - second_length] \
                               - prefix_sum[i - first_length - second_length]
            max_left_sum = max(max_left_sum, current_left_sum)
            right_sum = prefix_sum[i] - prefix_sum[i - second_length]
            max_sum = max(max_sum, max_left_sum + right_sum)

        return max_sum
