from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        sum_so_far = 0
        count = 0
        sum_mapping = {0: 1}

        for n in nums:
            sum_so_far += n

            if sum_so_far - goal in sum_mapping:
                count += sum_mapping[sum_so_far - goal]

            sum_mapping[sum_so_far] = sum_mapping.get(sum_so_far, 0) + 1

        return count
