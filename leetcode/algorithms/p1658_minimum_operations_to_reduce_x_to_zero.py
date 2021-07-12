from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = -x + sum(nums)
        total_sum = 0
        sum_mapping = {0: -1}
        max_length = 0

        if target == 0:
            return len(nums)

        for i, n in enumerate(nums):
            total_sum += n

            if total_sum - target in sum_mapping:
                current_length = i - sum_mapping.get(total_sum - target)
                max_length = max(max_length, current_length)

            sum_mapping[total_sum] = i

        return -1 if max_length == 0 else len(nums) - max_length
