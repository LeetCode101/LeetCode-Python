from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        counts = {0: 1}
        prefix = 0
        count = 0

        for n in nums:
            prefix = (prefix + n) % k
            count += counts.get(prefix, 0)
            counts[prefix] = counts.get(prefix, 0) + 1

        return count
