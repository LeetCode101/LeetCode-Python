from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sum = 0
        mapping = {0: 1}
        count = 0

        for i, n in enumerate(nums):
            sum += n
            key = sum if k == 0 else sum % k
            count += mapping.get(key, 0)
            mapping[key] = mapping.get(key, 0) + 1

        return count
