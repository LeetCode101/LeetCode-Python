from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sum_so_far = 0
        mapping = {0: 1}
        count = 0

        for i, n in enumerate(nums):
            sum_so_far += n
            key = sum_so_far if k == 0 else sum_so_far % k
            count += mapping.get(key, 0)
            mapping[key] = mapping.get(key, 0) + 1

        return count
