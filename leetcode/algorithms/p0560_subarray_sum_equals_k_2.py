from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_so_far = 0
        count = 0
        sum_mapping = {0: 1}

        for n in nums:
            sum_so_far += n

            if sum_so_far - k in sum_mapping:
                count += sum_mapping[sum_so_far - k]

            sum_mapping[sum_so_far] = sum_mapping.get(sum_so_far, 0) + 1

        return count
