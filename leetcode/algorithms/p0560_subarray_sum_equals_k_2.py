from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = 0
        count = 0
        sum_mapping = {0: 1}

        for n in nums:
            sum += n

            if sum - k in sum_mapping:
                count += sum_mapping[sum - k]

            sum_mapping[sum] = sum_mapping.get(sum, 0) + 1

        return count
