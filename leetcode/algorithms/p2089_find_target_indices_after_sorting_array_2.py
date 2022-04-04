from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        less_count = 0
        equal_count = 0

        for n in nums:
            if n < target:
                less_count += 1
            elif n == target:
                equal_count += 1

        return list(range(less_count, less_count + equal_count))
