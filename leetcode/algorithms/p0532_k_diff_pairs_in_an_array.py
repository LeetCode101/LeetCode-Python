import collections
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        counter = collections.Counter(nums)
        count = 0

        for n, c in counter.items():
            if k == 0 and c >= 2:
                count += 1
            elif k > 0 and n + k in counter:
                count += 1

        return count
