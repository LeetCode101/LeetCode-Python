import collections
import sys
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = collections.defaultdict(int)
        min_value = sys.maxsize
        max_value = -sys.maxsize

        for n in nums:
            counter[n] += 1
            max_value = max(max_value, n)
            min_value = min(min_value, n)

        prev, current = 0, 0

        for i in range(min_value, max_value + 1):
            prev, current = current, max(current, prev + counter[i] * i)

        return current
